import os, json
from datetime import datetime
import pandas as pd
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from typing import Generator, Tuple
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
from decorators import logger, timeit_log
from module.llm_module import get_chat_model

@timeit_log
def get_hazop_fewshot_prompt():
    example_1 = {
        "reasoning": "The line from R-101 to S-101 handles hot vapors. If scrubber is blocked, pressure may rise.",
        "table": "R-101 → S-101,More,Pressure,High Pressure,Blocked scrubber,Overpressure → rupture,High,5,4,20,Critical,PSV + Scrubber Design,Medium,3,2,6,Medium,Install redundant vent line,2,1,2,Engineering"
    }

    example_2 = {
        "reasoning": "This utility water line feeds the scrubber. If the valve is misaligned, flow could reverse.",
        "table": "DWS → S-101,Reverse,Flow,Reverse Flow,Valve misalignment,Back-contamination of water system,Medium,3,3,9,Medium,Check valve,Low,2,2,4,Low,Add backflow preventer,1,1,1,Maintenance"
    }
    with open("data/sample_50_row_hazop_example.txt", "r", encoding="utf-8") as f:
        csv_text = f.read()

    example_3 = {
        "reasoning": "The line from R-101 to S-101 carries a hot process stream. An increase in heat exchanger failure could elevate downstream temperature.",
        "table": """R-101 → S-101,More,Temperature,High Temperature,Pump failure,Excessive heat due to pump failure,High,3,5,15,High,Manual operator rounds,Medium,2,4,8,Medium,Add alarm for high temp,2,4,8,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Valve stuck closed,Excessive heat due to valve stuck closed,Medium,5,2,10,Medium,BPCS loop,Low,4,1,4,Low,Update SOPs,4,1,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Valve stuck open,Excessive heat due to valve stuck open,Medium,3,4,12,Medium,Redundant sensors,Medium,2,3,6,Medium,Improve operator training,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Control valve failure,Excessive heat due to control valve failure,High,5,3,15,High,Temperature indicator; DCS alarm,Medium,4,2,8,Medium,Inspect heat exchanger tubes,4,2,8,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Abmormal source,Excessive heat due to abmormal source,High,4,4,16,High,High-temp trip,Medium,3,3,9,Medium,Install redundant control valve,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Blocked line,Excessive heat due to blocked line,High,5,5,25,High,High-temp trip,High,4,4,16,High,Install pressure relief valve,4,4,16,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Line rupture,Excessive heat due to line rupture,Medium,3,2,6,Medium,High-temp trip,Low,2,1,2,Low,Add alarm for high temp,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Leakage in pipe or flange,Excessive heat due to leakage in pipe or flange,High,4,4,16,High,Manual operator rounds,Medium,3,3,9,Medium,Improve cooling loop,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Air entrainment,Excessive heat due to air entrainment,High,4,4,16,High,Temperature indicator; DCS alarm,Medium,3,3,9,Medium,Install redundant control valve,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Vapor lock,Excessive heat due to vapor lock,Medium,4,3,12,Medium,Redundant sensors,Medium,3,2,6,Medium,Add alarm for high temp,3,2,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Cavitation,Excessive heat due to cavitation,High,5,3,15,High,Manual operator rounds,Medium,4,2,8,Medium,Install redundant control valve,4,2,8,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Flashing,Excessive heat due to flashing,Medium,3,3,9,Medium,Redundant sensors,Low,2,2,4,Low,Install redundant control valve,2,2,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Slug flow,Excessive heat due to slug flow,Medium,3,2,6,Medium,BPCS loop,Low,2,1,2,Low,Improve operator training,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Fouling in heat exchanger,Excessive heat due to fouling in heat exchanger,High,4,5,20,High,BPCS loop,Medium,3,4,12,Medium,Update SOPs,3,4,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Tube rupture in heat exchanger,Excessive heat due to tube rupture in heat exchanger,Medium,5,2,10,Medium,BPCS loop,Low,4,1,4,Low,Check insulation,4,1,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Cooling water failure,Excessive heat due to cooling water failure,Medium,4,2,8,Medium,Manual operator rounds,Low,3,1,3,Low,Improve operator training,3,1,3,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Steam supply failure,Excessive heat due to steam supply failure,High,4,4,16,High,Temperature indicator; DCS alarm,Medium,3,3,9,Medium,Improve cooling loop,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Instrument failure - sensor,Excessive heat due to instrument failure - sensor,High,4,5,20,High,Interlock system,Medium,3,4,12,Medium,Improve operator training,3,4,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Instrument failure - transmitter,Excessive heat due to instrument failure - transmitter,Medium,5,2,10,Medium,BPCS loop,Low,4,1,4,Low,Add alarm for high temp,4,1,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Instrument failure - controller,Excessive heat due to instrument failure - controller,High,4,4,16,High,Interlock system,Medium,3,3,9,Medium,Check insulation,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Instrument failure - valve actuator,Excessive heat due to instrument failure - valve actuator,High,3,5,15,High,BPCS loop,Medium,2,4,8,Medium,Improve operator training,2,4,8,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Instrument calibration drift,Excessive heat due to instrument calibration drift,Medium,3,4,12,Medium,Manual operator rounds,Medium,2,3,6,Medium,Update SOPs,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Controller setpoint error,Excessive heat due to controller setpoint error,Medium,3,4,12,Medium,BPCS loop,Medium,2,3,6,Medium,Improve operator training,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,PID tuning error,Excessive heat due to pid tuning error,High,5,3,15,High,Redundant sensors,Medium,4,2,8,Medium,Install pressure relief valve,4,2,8,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Power failure (main),Excessive heat due to power failure (main),Medium,4,3,12,Medium,Temperature indicator; DCS alarm,Medium,3,2,6,Medium,Improve operator training,3,2,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Power fluctuation or dip,Excessive heat due to power fluctuation or dip,High,5,4,20,High,BPCS loop,Medium,4,3,12,Medium,Add alarm for high temp,4,3,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,UPS failure,Excessive heat due to ups failure,Medium,5,2,10,Medium,Manual operator rounds,Low,4,1,4,Low,Adjust PID tuning,4,1,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Alarm failure,Excessive heat due to alarm failure,High,5,4,20,High,Manual operator rounds,Medium,4,3,12,Medium,Improve operator training,4,3,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Interlock logic error,Excessive heat due to interlock logic error,Medium,3,4,12,Medium,Control valve feedback,Medium,2,3,6,Medium,Improve operator training,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Interlock bypassed,Excessive heat due to interlock bypassed,Medium,3,3,9,Medium,Control valve feedback,Low,2,2,4,Low,Adjust PID tuning,2,2,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,PSV stuck closed,Excessive heat due to psv stuck closed,Medium,3,4,12,Medium,BPCS loop,Medium,2,3,6,Medium,Install redundant control valve,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,PSV stuck open,Excessive heat due to psv stuck open,High,5,5,25,High,Temperature indicator; DCS alarm,High,4,4,16,High,Improve operator training,4,4,16,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,PSV setpoint incorrect,Excessive heat due to psv setpoint incorrect,High,5,4,20,High,High-temp trip,Medium,4,3,12,Medium,Check insulation,4,3,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Human error - startup,Excessive heat due to human error - startup,Medium,5,2,10,Medium,Control valve feedback,Low,4,1,4,Low,Check insulation,4,1,4,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Human error - shutdown,Excessive heat due to human error - shutdown,High,4,4,16,High,Manual operator rounds,Medium,3,3,9,Medium,Update SOPs,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Human error - normal operation,Excessive heat due to human error - normal operation,Medium,3,4,12,Medium,Redundant sensors,Medium,2,3,6,Medium,Inspect heat exchanger tubes,2,3,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Operator misreads gauge,Excessive heat due to operator misreads gauge,High,4,4,16,High,BPCS loop,Medium,3,3,9,Medium,Improve operator training,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Incorrect manual valve alignment,Excessive heat due to incorrect manual valve alignment,High,4,5,20,High,Temperature indicator; DCS alarm,Medium,3,4,12,Medium,Update SOPs,3,4,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Maintenance error - reinstatement,Excessive heat due to maintenance error - reinstatement,High,4,4,16,High,Redundant sensors,Medium,3,3,9,Medium,Install pressure relief valve,3,3,9,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Maintenance error - bypass left open,Excessive heat due to maintenance error - bypass left open,Medium,3,2,6,Medium,Temperature indicator; DCS alarm,Low,2,1,2,Low,Check insulation,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Utility outage,Excessive heat due to utility outage,Medium,4,3,12,Medium,Interlock system,Medium,3,2,6,Medium,Update SOPs,3,2,6,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Incorrect mixing ratio,Excessive heat due to incorrect mixing ratio,High,5,5,25,High,BPCS loop,High,4,4,16,High,Check insulation,4,4,16,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Ambient temperature,Excessive heat due to ambient temperature,High,4,5,20,High,Manual operator rounds,Medium,3,4,12,Medium,Improve operator training,3,4,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Phase separation error,Excessive heat due to phase separation error,High,4,5,20,High,High-temp trip,Medium,3,4,12,Medium,Add alarm for high temp,3,4,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Tank overfill,Excessive heat due to tank overfill,High,5,4,20,High,Control valve feedback,Medium,4,3,12,Medium,Check insulation,4,3,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Wrong phase (liquid/vapor),Excessive heat due to wrong phase (liquid/vapor),Medium,3,2,6,Medium,BPCS loop,Low,2,1,2,Low,Improve operator training,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Wrong chemical added,Excessive heat due to wrong chemical added,Medium,3,2,6,Medium,BPCS loop,Low,2,1,2,Low,Check insulation,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Mixing incompatible materials,Excessive heat due to mixing incompatible materials,Medium,3,2,6,Medium,Control valve feedback,Low,2,1,2,Low,Update SOPs,2,1,2,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Safety relief device blocked,Excessive heat due to safety relief device blocked,High,5,4,20,High,BPCS loop,Medium,4,3,12,Medium,Update SOPs,4,3,12,Engineering
                    R-101 → S-101,More,Temperature,High Temperature,Incorrect procedure followed,Excessive heat due to incorrect procedure followed,High,3,5,15,High,Temperature indicator; DCS alarm,Medium,2,4,8,Medium,Improve cooling loop,2,4,8,Engineering"""
    }

    example_prompt = PromptTemplate(
        input_variables=["reasoning", "table"],
        template="Reasoning:\n{reasoning}\n\nCSV Row:\n{table}"
    )
    role_and_rules_2 = """
            You are a deterministic, regulation-compliant **Process Safety Engineer AI** that strictly follows IEC 61882 and Open-PHA CSV export standards.

            ───────────────────────────────────────────────────────
            OBJECTIVE
            Generate a fully auditable **HAZOP worksheet** in strict **UTF-8 comma-separated CSV** format — compatible with Open-PHA — for a single deviation.

            The deviation is defined by the supplied:
            • Node
            • Guide Word
            • Parameter
            • Line ID
            • Process Description

            ───────────────────────────────────────────────────────
            MANDATORY RULES (DO NOT BREAK)

            1. You must return **exactly 50 rows** per response — **no more, no less**.
            - Each row must contain one unique Cause from the **MANDATORY ENGINEERING CAUSE CHECKLIST**.
            - No omission, repetition, or reordering is allowed.
            - If fewer than 50 rows are returned, you will fail the task.

            2. Output format:
            • Return ONLY the 50 valid **CSV rows**, with 21 comma-separated fields in this exact order:
                ```
                Node, Guide Word, Parameter, Deviation, Cause, Consequence, Unmitigated Risk Category,
                S Before Safeguards, L Before Safeguards, RR Before Safeguards, Overall Risk,
                Safeguards, Mitigated Risk Category, S, L, RR, Overall Risk,
                Recommendations, S After Recommendation, L After Recommendation, RR After Recommendation, Responsibility
                ```
            • No Markdown, no code block fences, no headers, no comments.

            3. For each Cause:
            • Generate a specific, realistic **Consequence**.
            • Specify at least one relevant **Safeguard** (instrument, procedure, interlock, etc).
            • Provide a unique **Recommendation** directly linked to the Cause.
            • Assign **Unmitigated** and **Mitigated Risk**: use 1-5 for Severity (S) and Likelihood (L), compute RR = S * L.
            • Apply this Risk Matrix:
                - RR 1-4 = Low
                - RR 5-12 = Medium
                - RR 13-25 = High

            4. For any mathematical or category mismatch, silently correct it.

            5. Responsibility field must be "Engineering" or "Maintenance" or "Operations".

            6. You MUST auto-validate that 50 rows are output, each using a different Cause from the checklist.
            
            7. Row Count Validation: Before emitting output, silently count CSV lines. If ≠ 50, regenerate internally.

            ───────────────────────────────────────────────────────
            MANDATORY ENGINEERING CAUSE CHECKLIST (MUST appear once each)
            1. Pump failure  
            2. Valve stuck closed  
            3. Valve stuck open  
            4. Control valve failure  
            5. Abmormal source  
            6. Blocked line  
            7. Line rupture  
            8. Leakage in pipe or flange  
            9. Air entrainment  
            10. Vapor lock  
            11. Cavitation  
            12. Flashing  
            13. Slug flow  
            14. Fouling in heat exchanger  
            15. Tube rupture in heat exchanger  
            16. Cooling water failure  
            17. Steam supply failure  
            18. Instrument failure - sensor  
            19. Instrument failure - transmitter  
            20. Instrument failure - controller  
            21. Instrument failure - valve actuator  
            22. Instrument calibration drift  
            23. Controller setpoint error  
            24. PID tuning error  
            25. Power failure (main)  
            26. Power fluctuation or dip  
            27. UPS failure  
            28. Alarm failure  
            29. Interlock logic error  
            30. Interlock bypassed  
            31. PSV stuck closed  
            32. PSV stuck open  
            33. PSV setpoint incorrect  
            34. Human error - startup  
            35. Human error - shutdown  
            36. Human error - normal operation  
            37. Operator misreads gauge  
            38. Incorrect manual valve alignment  
            39. Maintenance error - reinstatement  
            40. Maintenance error - bypass left open  
            41. Utility outage  
            42. Incorrect mixing ratio  
            43. Ambient temperature  
            44. Phase separation error  
            45. Tank overfill  
            46. Wrong phase (liquid/vapor)  
            47. Wrong chemical added  
            48. Mixing incompatible materials  
            49. Safety relief device blocked  
            50. Incorrect procedure followed  

            ───────────────────────────────────────────────────────
            DO NOT continue if data is not between tags:

            <START-DATA>
            [ Line ID: {line_id}
            Node: {node}
            Valves: {valves}
            Instruments: {instruments}
            Context: {context}
            Process Description: {process_description}
            Guide Word: {guide_word}
            Parameter: {parameter}
            ]
            <END-DATA>
            -------------------------------------------------------------------------------
            EXAMPLE DEVIATION PAIRS  
            No + Flow → No Flow/ More + Pressure → High Pressure/ Other than + Composition → Off-Spec
            -------------------------------------------------------------------------------
            ───────────────────────────────────────────────────────
            FINAL INSTRUCTION
            Return 50 CSV rows only. Nothing else. Begin output below:


    """

    role_and_rules = """
        Act like the world's most deterministic, IEC 61882-compliant **Process Safety Engineer AI**.

        OBJECTIVE  
        • Generate a fully auditable, regulation-grade **HAZOP worksheet** in **strict UTF-8 comma-separated CSV** (Open-PHA compatible) using *only* the structured JSON that appears between the required tags.
        
        <START-DATA>
        [
            Line ID: {line_id}
            Node: {node}
            Valves: {valves}
            Instruments: {instruments}
            Context: {context}
            Process Description:
            {process_description}
        ]
        <END-DATA>

        Do **not** begin the HAZOP until JSON appears between the tags.

        -------------------------------------------------------------------------------
        GLOBAL RULES (enforced at every step)  
        1. Treat each object in the JSON array as a distinct **Node**.  
        2.  Form *Deviations* only by valid combinations of the **Guide Words** and **Parameters** provided below—never duplicate a word between the two lists. 
        3. For **every** Deviation, expand **all 50 Causes** from the mandatory checklist:**one unique row per cause, no omissions, no merging, no re-ordering**. 
        3.1 IMPORTANT 50-All MANDATORY ENGINEERING CAUSE CHECKLIST must be used and show in answer
        4. Every CSV cell must contain concrete, specific text—no “TBD”, blanks, or generic statements.  
        5. **Risk Rating (RR)** = Severity * Likelihood. Map RR → Risk Category (Low, Medium, High) using the embedded 5*5 matrix. 
        6. Each Recommendation must directly address its corresponding Cause. 
        7. Autovalidate logic before release; silently correct any math error,category mis-alignment, or Guide-Word/Parameter mismatch.
        8. **Output only the CSV data rows**—no headers, commentary, Markdown, or code-block fences.
   
        -------------------------------------------------------------------------------
        APPROVED GUIDE WORDS  
        • {guide_word}  

        APPROVED PARAMETERS  
        • {parameter}  

        EXAMPLE DEVIATION PAIRS  
        No + Flow → No Flow/ More + Pressure → High Pressure/ Other than + Composition → Off-Spec
        
        -------------------------------------------------------------------------------
        MANDATORY ENGINEERING CAUSE CHECKLIST (appear **verbatim**—exactly once per Deviation) 
        Use the following 50 causes **internally**; they must each appear once per Deviation.  
        1. Pump failure  
        2. Valve stuck closed  
        3. Valve stuck open  
        4. Control valve failure  
        5. Abmormal source  
        6. Blocked line  
        7. Line rupture  
        8. Leakage in pipe or flange  
        9. Air entrainment  
        10. Vapor lock  
        11. Cavitation  
        12. Flashing  
        13. Slug flow  
        14. Fouling in heat exchanger  
        15. Tube rupture in heat exchanger  
        16. Cooling water failure  
        17. Steam supply failure  
        18. Instrument failure - sensor  
        19. Instrument failure - transmitter  
        20. Instrument failure - controller  
        21. Instrument failure - valve actuator  
        22. Instrument calibration drift  
        23. Controller setpoint error  
        24. PID tuning error  
        25. Power failure (main)  
        26. Power fluctuation or dip  
        27. UPS failure  
        28. Alarm failure  
        29. Interlock logic error  
        30. Interlock bypassed  
        31. PSV stuck closed  
        32. PSV stuck open  
        33. PSV setpoint incorrect  
        34. Human error - startup  
        35. Human error - shutdown  
        36. Human error - normal operation  
        37. Operator misreads gauge  
        38. Incorrect manual valve alignment  
        39. Maintenance error - reinstatement  
        40. Maintenance error - bypass left open  
        41. Utility outage  
        42. Incorrect mixing ratio  
        43. Ambient temperature  
        44. Phase separation error  
        45. Tank overfill  
        46. Wrong phase (liquid/vapor)  
        47. Wrong chemical added  
        48. Mixing incompatible materials  
        49. Safety relief device blocked  
        50. Incorrect procedure followed  
        *(Checklist is for your reference only— refine act like human by follow data in <START-DATA>..<END-DATA>.)*

        -------------------------------------------------------------------------------
        STEP-BY-STEP WORKFLOW
        **Step 0 - Data Ingestion**  
        • Parse the JSON array between <START-DATA>…<END-DATA>. 
        • Store: Line ID, Node, Valves, Instruments, Context, Process Description.

        **Step 1 - Parameter Identification**  
        • Derive the applicable *Parameters* for each Node using Context + Process Description.

        **Step 2 - Deviation Generation**  
        • Pair each identified **APPROVED PARAMETERS** with every valid **APPROVED GUIDE WORDS** to create Deviations.

        **Step 3 - Cause Expansion**  
        • For each Deviation, output 50 rows—one for each Cause in the checklist and **All 50-MANDATORY ENGINEERING CAUSE CHECKLIST must be used and show in output**.

        **Step 4 - Consequence, Safeguard & Recommendation**  
        • Craft a Node-specific engineering-realistic Consequence for each Cause. 
        • Enumerate all explicit or implied Safeguards (valves, instruments, interlocks, procedures); separate multiples with semicolons. 
        • Propose one actionable Recommendation that directly mitigates the Cause.

        **Step 5 - Risk Evaluation (Unmitigated & Mitigated)**  
        • Assign Severity (S) and Likelihood (L) before safeguards; compute RR and Category.  
        • Re-evaluate S and/or L *after* implementing the Recommendation; recalculate RR and Category.

        **Step 6 - CSV Assembly**  
        Populate **exactly** these 21 columns **in the order shown**—omit the header row:  
        Node, Guide Word, Parameter, Deviation, Cause, Consequence, Unmitigated Risk Category, S Before Safeguards, L Before Safeguards, RR Before Safeguards, Overall Risk, Safeguards, Mitigated Risk Category, S, L, RR, Overall Risk, Recommendations, S After Recommendation, L After Recommendation, RR After Recommendation, Responsibility

        **Step 7 - Validation Loop**  
        • Auto-check every row for completeness, uniqueness, logical consistency, math correctness, and category alignment.  
        • Iterate silently until *All-output-answer must have 50 cause in checklist* checks pass.

        **Step 8 - Output**  
        • Emit the CSV data rows *only*—no header, no extra text, no Markdown fences.

        -------------------------------------------------------------------------------
        RISK MATRIX (5*5 example)  
        Severity (1-5) * Likelihood (1-5) → RR  
        1-4 = Low / 5-12 = Medium/ 13-25 = High  

        -------------------------------------------------------------------------------
        CONFIDENTIALITY  
        All chain-of-thought, intermediate reasoning, calculations, and notes must remain internal.
        Expose **only** the validated CSV output.

        Take a deep breath and work on this problem step-by-step.
        """

    cot_suffix = """
        Analyze the line below using HAZOP methodology.

        Line ID: {line_id}
        Node: {node}
        Valves: {valves}
        Instruments: {instruments}
        Context: {context}
        Process Description:
        {process_description}
        Parameter: {parameter}
        Guide Word: {guide_word}

        Remember: You must output exactly 50 rows,each with 21 comma-separated fields. If any field is not applicable, use "N/A". Never skip a Cause. Never leave cells blank.
        Think step-by-step before generating the CSV.
        Return only valid CSV rows in UTF-8 format (no markdown, no commentary).
        """

    few_shot_prompt = FewShotPromptTemplate(
        prefix=role_and_rules_2.strip(),
        suffix=cot_suffix.strip(),
        examples=[example_3],
        example_prompt=example_prompt,
        input_variables=["line_id", "node", "valves", "instruments", "context", "process_description"]
    )

    return few_shot_prompt

def get_hazop_other_prompt():
    example_2 = {
        "reasoning": (
            "The HF/BF₃ feed line uses N₂ as an inert purge, but HF and BF₃ are "
            "extremely corrosive—moisture traces form hydrofluoric and boron-fluoride "
            "acids that aggressively thin carbon-steel walls. Progressive wall-loss can "
            "go unnoticed until a through-wall defect occurs, releasing a toxic, high-pressure "
            "HF/BF₃ mixture. Therefore pipeline corrosion is a credible cause of rupture or leakage."
        ),
        "table": (
            "Process,Other,Process,Others,"
            "Pipeline corrosion,Pipeline rupture/leakage,"
            "High,4,3,12,Critical,"
            "Corrosion protection coating and periodic inspection,"
            "Medium,4,2,8,Medium,"
            "Replace gaskets and schedule regular maintenance,3,2,6,Maintenance Engineer"
        )
    }

    example_prompt = PromptTemplate(
        input_variables=["reasoning", "table"],
        template="Reasoning:\n{reasoning}\n\nCSV Row:\n{table}"
    )

    role_and_rules = """
        Act like the world's most deterministic, IEC 61882-compliant **Process Safety Engineer AI**.
        ────────────────────────────────────────────────────────
        OBJECTIVE
        Generate a fully auditable, regulation-grade **HAZOP worksheet** in **strict UTF-8 comma-separated CSV** (Open-PHA compatible) using *only* the structured JSON provided between the required tags.

        <START-DATA>
        [
            System input: {system_input}
            System output: {system_output}
            Process Description: {process_description}
        ]
        <END-DATA>

        ────────────────────────────────────────────────────────
        GLOBAL RULES & FORMAT CONSTRAINTS
        1. **NO headers, Markdown, comments, or extra lines** — output *only* CSV data rows.
        2. Encode strictly in UTF-8; use a literal comma (,) as the sole delimiter.
        3. Populate **exactly 21 columns in this order**:  
        Node, Guide Word, Parameter, Deviation, Cause, Consequence, Unmitigated Risk Category, S Before Safeguards, L Before Safeguards, RR Before Safeguards, Overall Risk, Safeguards, Mitigated Risk Category, S, L, RR, Overall Risk, Recommendations, S After Recommendation, L After Recommendation, RR After Recommendation, Responsibility
        4. Compute Risk Rank (RR) as **Severity * Likelihood**; map to Category: *Low 1-4*, *Medium 5-12*, *High 13-25*.
        5. **Mandatory Engineering Cause Checklist** (appear verbatim, once per Deviation, exactly this order): -- Must using all Cause Checklist***
        5.1. Pipeline corrosion  
        5.2. Power outage.  
        5.3. Static electricity.  
        5.4. Natural disasters (earthquake, lightning, typhoon).  
        5.5. Human operational error.  
        5.6. Personnel poisoning
        6. Use **Guide Word = “Others”** for every row.
        7. **Silently self-validate**: uniqueness, completeness, logical consistency, math accuracy, category alignment. Iterate until every check passes.
        8. **Confidentiality**: keep all reasoning internal; expose only the final CSV rows.

        ────────────────────────────────────────────────────────
        STEP-BY-STEP WORKFLOW
        **Step 0 - Pre-Check**  
        • Verify JSON is well-formed; reject processing if tags or syntax are invalid.

        **Step 1 - Parameter Derivation**  
        • From *System input/output* and *Process Description*, list the key process parameters relevant to each equipment or pipeline Node (flow, pressure, temperature, composition, etc.).

        **Step 2 - Node/Deviation Construction**  
        • For  Node using "Process", pair Parameter "Process" with Guide Word “Others” to generate a single clear Deviation phrase.

        **Step 3 - Cause Expansion**  
        • For each Deviation create **six rows**, using every Cause in the **Mandatory Engineering Cause Checklist** (5.1-5.6) exactly once.

        **Step 4 - Consequence, Safeguard & Recommendation**  
        • Craft a realistic, Node-specific engineering Consequence for the given Cause.  
        • List all explicit or implied Safeguards (valves; instruments; interlocks; procedures); separate multiples with semicolons.  
        • Propose one actionable Recommendation that directly mitigates this Cause.

        **Step 5 - Risk Evaluation**  
        • Assign pre-safeguard Severity (S 1-5) and Likelihood (L 1-5); compute RR and Category.  
        • After Recommendation, reassess S and/or L; recompute RR and Category.

        **Step 6 - CSV Assembly**  
        • Populate each of the 21 columns per Rule 3 with validated data.

        **Step 7 - Validation Loop**  
        • Auto-check every row for completeness, uniqueness, logical consistency, math correctness, and category alignment; iterate silently until *all* rows pass.

        **Step 8 - Output**  
        • Emit the final CSV rows only, with no headers or extra text.

        ────────────────────────────────────────────────────────
        RISK MATRIX (5 * 5)  
        Severity (1-5) * Likelihood (1-5) → RR  
        1-4 = Low | 5-12 = Medium | 13-25 = High  

        ────────────────────────────────────────────────────────
        Take a deep breath and work on this problem step-by-step.
        """

    cot_suffix = """
        Analyze the line below using HAZOP methodology.

        System input: {system_input}
        System output: {system_output}
        Process Description: {process_description}

        Think step-by-step before generating the CSV.
        Return only valid CSV rows in UTF-8 format (no markdown, no commentary).
        """

    few_shot_other = FewShotPromptTemplate(
        prefix=role_and_rules.strip(),
        suffix=cot_suffix.strip(),
        examples=[example_2],
        example_prompt=example_prompt,
        input_variables=["system_input", "system_output", "process_description"]
    )

    return few_shot_other

def list_all_process(pid_data: dict):
    parsed = pid_data["choices"][0]["message"]["parsed"]

    system_input = parsed.get("system_inputs", [])
    system_output = parsed.get("system_outputs", [])
    process_description = parsed.get("process_description", "")

    query_infos = []
    query_infos.append({
        "system_input": system_input,
        "system_output": system_output,
        "process_description": process_description
    })
    return query_infos

def list_all_connections(pid_data: dict):
    parsed = pid_data["choices"][0]["message"]["parsed"]
    connections = parsed.get("connections", [])
    process_description = parsed.get("process_description", "")
    
    query_infos = []
    for conn in connections:
        line_id = conn["line_id"]
        from_id = conn.get("from_id")
        to_id = conn.get("to_id")
        node = f"{from_id} → {to_id}"
        context = conn.get("context", "")
        valves = conn.get("valves", [])
        instruments = conn.get("instruments", [])
        
        query_infos.append({
            "line_id": line_id,
            "node": node,
            "valves": valves,
            "instruments": instruments,
            "context": context,
            "process_description": process_description
        })
    return query_infos

@timeit_log
def run_hazop_agent(pid_data: dict, excel_path: str, token_log_path: str, error_log_path: str,
                    llm_response_log_path: str, parsed_excel_path: str, token_limit: int = 10000
                   ) -> Generator[Tuple[str, int], None, None]:

    def parse_llm_result_to_rows(result_text: str) -> list:
        rows = []
        for line in str(result_text).strip().splitlines():
            parts = [cell.strip() for cell in line.split(",")]
            if len(parts) == len(headers):
                rows.append(parts)
        return rows
    
    @timeit_log
    def parse_llm_result(raw_out: str, i=5) -> list:
        parts = [p.strip() for p in raw_out.split(",")]
        result = {col: "" for col in headers}

        result["Node"] = parts[0]
        result["Guide Word"] = parts[1] if parts[1] in guide_ws else ""
        result["Parameter"] = parts[2] if parts[2] in params else ""
        result["Deviation"] = parts[3]
        result["Cause"] = parts[4]

        conseq = []
        safeg = []
        recomm = []

        while i < len(parts):
            if parts[i] in valid_risk_categories:
                result["Unmitigated Risk Category"] = parts[i]
                break
            else:
                conseq.append(parts[i])
            i += 1
        result["Consequence"] = "; ".join(conseq)

        result["S Before Safeguards"] = int(parts[i+1]) if parts[i+1].isdigit() else parts[i+1]
        result["L Before Safeguards"] = int(parts[i+2]) if parts[i+2].isdigit() else parts[i+2]
        result["RR Before Safeguards"] = int(parts[i+3]) if parts[i+3].isdigit() else parts[i+3]
        result["Overall Risk"] = parts[i+4]

        j = i + 5
        while j < len(parts):
            if parts[j] in valid_risk_categories:
                result["Mitigated Risk Category"] = parts[j]
                break
            else:
                safeg.append(parts[j])
            j += 1
        result["Safeguards"] = "; ".join(safeg)

        result["S"] = int(parts[j+1]) if parts[j+1].isdigit() else parts[j+1]
        result["L"] = int(parts[j+2]) if parts[j+2].isdigit() else parts[j+2]
        result["RR"] = int(parts[j+3]) if parts[j+3].isdigit() else parts[j+3]
        result["Overall Risk"] = parts[j+4]

        k = j + 5
        while k < len(parts) - 4:
            recomm.append(parts[k])
            k += 1
        result["Recommendations"] = "; ".join(recomm)

        result["S After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["L After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["RR After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["Responsibility"] = parts[k]

        return [[result[col] for col in headers]]

    query_infos = list_all_connections(pid_data)
    valid_risk_categories = ["Low", "Medium", "High", "N/A"]
    parsed_rows = []
    headers = [
        "Node", "Guide Word", "Parameter", "Deviation", "Cause", "Consequence", 
        "Unmitigated Risk Category", "S Before Safeguards", "L Before Safeguards", 
        "RR Before Safeguards", "Overall Risk", "Safeguards", "Mitigated Risk Category", 
        "S", "L", "RR", "Overall Risk", "Recommendations", "S After Recommendation", 
        "L After Recommendation", "RR After Recommendation", "Responsibility"
    ]

    df = pd.read_excel(excel_path) if os.path.exists(excel_path) else pd.DataFrame(columns=headers)
    token_df = pd.read_csv(token_log_path) if os.path.exists(token_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "Model", "PromptTokens", "CompletionTokens", "TotalTokens"
    ])
    error_df = pd.read_csv(error_log_path) if os.path.exists(error_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput", "Reason"
    ])
    llm_response_df = pd.read_csv(llm_response_log_path) if os.path.exists(llm_response_log_path) else pd.DataFrame(columns=[
        "Timestamp", "LineID", "Parameter", "GuideWord", "RawOutput"
    ])

    llm, model_name = get_chat_model()
    hazop_chain = LLMChain(llm=llm, prompt=get_hazop_fewshot_prompt())
    guide_ws_t = ["No","More","Less","As well as","Part of","Reverse","Other than","Early","Late","Before","After"]
    params_t = ["Flow","Pressure","Temperature","Level","Composition","Phase","Utility","Power","Instrument","Human Action","Maintenance","Operation Timing", "Concentration"]
    guide_ws = ["More"]
    params = ["Pressure"]

    for info in query_infos:
        if info["line_id"] not in ["L02"]:
            continue

        for param in params:
            for guide_word in guide_ws:
                input_data = {
                    "line_id": info["line_id"],
                    "node": info["node"],
                    "valves": ", ".join(info.get("valves", [])),
                    "instruments": ", ".join(info.get("instruments", [])),
                    "context": info.get("context", ""),
                    "process_description": info["process_description"],
                    "parameter": param,
                    "guide_word": guide_word,
                }

                with get_openai_callback() as cb:
                    try:
                        result = hazop_chain.run(**input_data)

                        # Parse result into structured rows
                        rows = []
                        for line in result.strip().splitlines():
                            rows += parse_llm_result(line)

                        parsed_rows.extend(rows)

                    except Exception as e:
                        logger.error(f"[Error] {info['line_id']}:{param}:{guide_word} — {e}")
                        continue

                    if cb.total_tokens > token_limit:
                        logger.warning(f"[Skipped] {info['line_id']}:{param}:{guide_word} — {cb.total_tokens} tokens")
                        continue

                    tokens_used = cb.total_tokens

                # Log RawOutput
                response_entry = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "LineID": info["line_id"],
                    "Parameter": param,
                    "GuideWord": guide_word,
                    "RawOutput": result
                }
                llm_response_df = pd.concat([llm_response_df, pd.DataFrame([response_entry])], ignore_index=True)
                llm_response_df.to_csv(llm_response_log_path, index=False)

                # Parse LLM output
                # parsed_rows = parse_llm_result(result)

                if not parsed_rows:
                    print(f"[Warning] No valid rows for {info['line_id']}:{param}:{guide_word}")
                    error_entry = {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "LineID": info["line_id"],
                        "Parameter": param,
                        "GuideWord": guide_word,
                        "RawOutput": result,
                        "Reason": f"Invalid or no rows parsed (expected {len(headers)} columns)"
                    }
                    error_df = pd.concat([error_df, pd.DataFrame([error_entry])], ignore_index=True)
                    error_df.to_csv(error_log_path, index=False)
                    continue

                # Token log
                token_row = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "LineID": info["line_id"],
                    "Parameter": param,
                    "GuideWord": guide_word,
                    "Model": model_name,
                    "PromptTokens": cb.prompt_tokens,
                    "CompletionTokens": cb.completion_tokens,
                    "TotalTokens": cb.total_tokens
                }
                token_df = pd.concat([token_df, pd.DataFrame([token_row])], ignore_index=True)
                token_df.to_csv(token_log_path, index=False)

                # Append to parsed output log
                df_parsed = pd.DataFrame(parsed_rows, columns=headers)
                if os.path.exists(parsed_excel_path):
                    df_existing = pd.read_excel(parsed_excel_path)
                    df_combined = pd.concat([df_existing, df_parsed], ignore_index=True)
                else:
                    df_combined = df_parsed
                df_combined.to_excel(parsed_excel_path, index=False)

                # Append to main HAZOP output
                df = pd.concat([df, df_parsed], ignore_index=True)
                df.to_excel(excel_path, index=False)

                yield f"{info['line_id']}:{param}:{guide_word}", tokens_used


def run_hazop_agent_other(pid_data: dict, excel_path: str, token_log_path: str, token_limit: int = 10000) -> Generator[Tuple[str, int], None, None]:
    
    query_infos = list_all_process(pid_data)

    parsed = pid_data["choices"][0]["message"]["parsed"]
    system_input = parsed.get("system_inputs", [])
    system_output = parsed.get("system_outputs", [])

    for info in query_infos:
        info["system_input"] = system_input
        info["system_output"] = system_output

    headers = [
        "Node", "Guide Word", "Parameter", "Deviation", "Cause", "Consequence", 
        "Unmitigated Risk Category", "S Before Safeguards", "L Before Safeguards", 
        "RR Before Safeguards", "Overall Risk", "Safeguards", "Mitigated Risk Category", 
        "S", "L", "RR", "Overall Risk", "Recommendations", "S After Recommendation", 
        "L After Recommendation", "RR After Recommendation", "Responsibility"
    ]

    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path)
    else:
        df = pd.DataFrame(columns=headers)

    if os.path.exists(token_log_path):
        token_df = pd.read_csv(token_log_path)
    else:
        token_df = pd.DataFrame(columns=[
            "Timestamp", "LineID", "Model", "PromptTokens", "CompletionTokens", "TotalTokens"
        ])

    llm, model_name = get_chat_model()
    hazop_chain = LLMChain(llm=llm, prompt=get_hazop_other_prompt())
    total_tokens_used = 0

    for info in query_infos:

        input_data = {
            "system_input": info["system_input"],
            "system_output": info["system_output"],
            "process_description": info["process_description"]
        }

        with get_openai_callback() as cb:
            try:
                result = hazop_chain.run(**input_data)
            except Exception as e:
                print(f"[Error] {info['line_id']} — {e}")
                continue

            if cb.total_tokens > token_limit:
                print(f"[Skipped] {info['line_id']} — {cb.total_tokens} tokens (exceeds per-run limit: {token_limit})")
                continue

            tokens_used = cb.total_tokens

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            token_row = {
                "Timestamp": timestamp,
                "LineID": info["system_input"],
                "Model": model_name,
                "PromptTokens": cb.prompt_tokens,
                "CompletionTokens": cb.completion_tokens,
                "TotalTokens": cb.total_tokens
            }
            token_df = pd.concat([token_df, pd.DataFrame([token_row])], ignore_index=True)
            token_df.to_csv(token_log_path, index=False)

        print(f"[Processed] {info["system_input"]} — {tokens_used} tokens (Total: {total_tokens_used})")

        rows = result.strip().splitlines()
        parsed_rows = [
            r.split(",") for r in rows 
            if len(r.strip()) > 0 and len(r.split(",")) == len(headers)
        ]

        if not parsed_rows:
            print(f"[Warning] No valid rows for {info["system_input"]}")
            continue

        temp_df = pd.DataFrame(parsed_rows, columns=headers)
        df = pd.concat([df, temp_df], ignore_index=True)
        df.to_excel(excel_path, index=False)

        yield info["system_input"], tokens_used