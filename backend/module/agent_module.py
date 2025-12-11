import os
from datetime import datetime
from typing import Generator, Tuple, List, Dict
import pandas as pd

from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from typing import Generator, Tuple
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

from decorators import logger, timeit_log
from module.llm_module import get_chat_model
import sys
sys.stdout.reconfigure(encoding="utf-8")

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
    with open("static/file/sample_50_row_hazop_example.txt", "r", encoding="utf-8") as f:
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

            1. You must return **exactly as many rows as there are causes in the MANDATORY ENGINEERING CAUSE CHECKLIST** — no more, no less.  
            - Each row must contain one unique Cause from the checklist.  
            - All listed causes (1 through N) must appear once — no omission, duplication, or reordering.  
            - Row count must always equal the number of causes in the checklist (auto-calculate N).

            2. Output format:
            • Return ONLY valid CSV rows, with **22 comma-separated fields** in this exact order:
                ```
                Node, Guide Word, Parameter, Deviation, Cause, Consequence, Unmitigated Risk Category,
                S Before Safeguards, L Before Safeguards, RR Before Safeguards, Overall Risk,
                Safeguards, Mitigated Risk Category, S, L, RR, Overall Risk,
                Recommendations, S After Recommendation, L After Recommendation, RR After Recommendation, Responsibility
                ```
            • No Markdown, no code block fences, no headers, no comments.

            3. For each Cause:
            • Generate a specific, realistic **Consequence**, including chemical/material hazards by check Input/Output Substance where relevant:
                - Personnel poisoning, corrosion, burns, asphyxiation  
                - Environmental pollution (air/water/soil)  
                - Explosion, fire, runaway reaction  
                - Process equipment damage/failure  
                - Product Quality
            • Specify at least one relevant **Safeguard** (instrument, procedure, interlock, etc).
            • Provide a unique **Recommendation** directly linked to the Cause.
            • Assign **Unmitigated** and **Mitigated Risk**:
                Severity S: S5 fatality/off-site env loss>300M/dt>6mo; S4 permanent disability/neighbor env loss30-300M/dt1-6mo; S3 treatable injury/area env loss3-30M/dt1-4wk; S2 minor injury/unit loss0.015-3M/dt4h-1wk; S1 negligible/equip loss<0.015M/dt<4h. Likelihood L: L5 often p≥1e-1; L4 likely 1e-1>p≥1e-2; L3 unlikely 1e-2>p≥1e-3; L2 very unlikely 1e-3>p≥1e-4; L1 extremely unlikely p<1e-4. Risk Matrix RL(S,L): S5:5,5,4,3,2; S4:5,4,4,3,2; S3:4,4,3,3,2; S2:3,3,3,2,1; S1:2,2,2,1,1. Risk Category: RL1-2 Low; RL3-4 Medium; RL5 High. RR fields return RL 1-5 only.
                RL meaning: 1-2 Low; 3-4 Medium; 5 High. and RL IS REPRESENT BY RR in (RR Before Safeguards,RR,RR After Recommendation) AND MAP BY Risk Level Matrix (S*L → RL):
                and IMPORTANT** (RR Before Safeguards,RR,RR After Recommendation) RETURN ONLY 1-5 MAP BY Risk Level Matrix:
            • Apply this For Unmitigated Risk Category , Mitigated Risk Category followed from Risk Level Matrix (S*L → RL) **RETURN ONLY Low, Medium, High or N/A**:
                - RL 1-2 = Low
                - RL 3-4 = Medium
                - RL 5 = High
            4. For any mathematical or category mismatch, silently correct it.

            5. Responsibility field must be "Engineering" or "Maintenance" or "Operations".

            6. You MUST auto-validate that 50 rows are output, each using a different Cause from the checklist.
            
            7. Row Count Validation: Before emitting output, silently count CSV lines. If ≠ NUMBER OF MANDATORY ENGINEERING CAUSE CHECKLIST, regenerate internally.

            ───────────────────────────────────────────────────────
            MANDATORY ENGINEERING CAUSE CHECKLIST (MUST appear once each)
            1.Pressure instrument failure (gauge; transmitter; sensor)
            2.Temperature instrument failure (thermometer; transmitter; sensor)
            3.Level instrument failure (indicator; transmitter; sensor)
            4.Flow instrument failure (meter; sensor; transmitter)
            5.Incorrect instrument calibration or setpoint
            6.Control valve malfunction (stuck; leakage; actuator failure)
            7.Incorrect valve selection or specification
            8.Proportional/regulating valve malfunction
            9.Pneumatic valve failure or loss of actuator signal
            10.Vent valve malfunction (fails closed/open during transfer or discharge)
            11.Pipeline leakage (joint failure; crack; corrosion; gasket)
            12.Pipeline blockage or obstruction (fouling; deposits; freezing; solids)
            13.Incorrect installation or poor layout of piping/equipment
            14.Vessel leakage or rupture (design or fatigue failure)
            15.Pump mechanical failure (seal; impeller; shaft; cavitation)
            16.Compressor or fan mechanical failure (motor; bearing; impeller)
            17.Vacuum pump failure (cannot achieve required vacuum)
            18.Refrigerant/utility line rupture or internal leak
            19.Cylinder rupture or containment breach
            20.Drain hole blockage or inadequate drainage
            21.Equipment overheating (heater runaway; thermal stress)
            22.Abnormal wear/erosion leading to loss of containment
            23.Abnormal utility supply pressure (too high or too low)
            24.Abnormal cryogenic source (LN2 evaporation; boil-off; loss of supply)
            25.Abnormal water supply (insufficient cooling or cleaning water)
            26.Abnormal gas supply (N₂; compressed air; other utility failure)
            27.Power failure (loss of electricity to motors; fans; instruments)
            28.Cooling system failure (no circulation; fouling; exchanger blocked)
            29.Heating system failure (heater not starting or insufficient duty)
            30.Heating system uncontrolled (heater operating without cutoff)
            31.Utility connection leakage (joints; hoses; couplings)
            32.Pressure regulator malfunction (failure of PRV or regulator valve)
            33.Upstream overpressure (abnormal feed source pressure)
            34.Downstream restriction (blockage; closed valve; isolation)
            35.Reverse flow due to pressure imbalance or check valve failure
            36.Reaction runaway / abnormal process temperature rise
            37.Abnormal mixing ratio (incorrect blending; poor agitation)
            38.Incorrect feed ratio or dosage deviation
            39.Abnormal circulation imbalance (inlet > outlet; unequal flows)
            40.Vessel operating empty or insufficient level (dry running)
            41.Vessel operating overfilled (high level)
            42.Internal decomposition of process medium (gas release; thermal breakdown)
            43.Ambient high temperature (external fire; hot weather)
            44.Ambient low temperature (cold weather; freezing)
            45.External mechanical impact or vibration
            46.Abnormal source contamination (impurities; off-spec feed)
            47.Human error in operation (wrong valve; wrong sequence)
            48.Incorrect operating sequence (early or late action)
            49.Insufficient operating time (too short cycle; premature termination)
            50.Excessive operating time (too long cycle, delayed termination) 

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
    # --- Detect shape ---
    if "choices" in pid_data:
        # old style: OpenAI chat completion wrapper
        parsed = pid_data["choices"][0]["message"]["parsed"]
    elif "pid_data" in pid_data and isinstance(pid_data["pid_data"], dict):
        # new style: your file wrapper with metadata
        parsed = pid_data["pid_data"]
    else:
        # already the bare P&ID JSON
        parsed = pid_data

    connections = parsed.get("connections", [])
    process_description = parsed.get("process_description", "")

    query_infos = []
    for conn in connections:
        line_id = conn.get("line_id")
        from_id = conn.get("from_id")
        to_id = conn.get("to_id")
        node = f"{from_id} → {to_id}" if from_id and to_id else (from_id or to_id or "")
        context = conn.get("context", "")
        valves = conn.get("valves", [])
        instruments = conn.get("instruments", [])

        query_infos.append(
            {
                "line_id": line_id,
                "node": node,
                "valves": valves,
                "instruments": instruments,
                "context": context,
                "process_description": process_description,
            }
        )
    return query_infos

@timeit_log
def run_hazop_agent(
    pid_data: dict,
    excel_path: str,
    token_log_path: str,
    error_log_path: str,
    llm_response_log_path: str,
    parsed_excel_path: str,
    selections: List[Dict[str, str]],  # NEW
    token_limit: int = 20000,
) -> Generator[Tuple[str, int], None, None]:
    valid_guide_ws = [
        "No", "More", "Less", "As well as", "Part of", "Reverse",
        "Other than", "Early", "Late", "Before", "After", "No/Low"
    ]

    valid_params = [
        "Flow", "Pressure", "Temperature", "Level", "Composition",
        "Phase", "Utility", "Power", "Instrument", "Human Action",
        "Maintenance", "Operation Timing", "Concentration"
    ]

    # --- 1) Your detailed single-line parser (unchanged logic) ---
    @timeit_log
    def parse_llm_result(raw_out: str, i: int = 5) -> list[list[str]]:
        parts = [p.strip() for p in str(raw_out).split(",")]
        result = {col: "" for col in headers}

        # base fields
        result["Node"] = parts[0]
        result["Guide Word"] = parts[1] if parts[1] in valid_guide_ws else ""
        result["Parameter"] = parts[2] if parts[2] in valid_params else ""
        result["Deviation"] = parts[3]
        result["Cause"] = parts[4]

        conseq: list[str] = []
        safeg: list[str] = []
        recomm: list[str] = []

        # --- Consequence + Unmitigated Risk Category ---
        while i < len(parts):
            if parts[i] in valid_risk_categories:
                result["Unmitigated Risk Category"] = parts[i]
                break
            else:
                conseq.append(parts[i])
            i += 1
        result["Consequence"] = "; ".join(conseq)

        # S/L/RR before safeguards + Overall Risk (unmitigated)
        result["S Before Safeguards"] = int(parts[i + 1]) if parts[i + 1].isdigit() else parts[i + 1]
        result["L Before Safeguards"] = int(parts[i + 2]) if parts[i + 2].isdigit() else parts[i + 2]
        result["RR Before Safeguards"] = int(parts[i + 3]) if parts[i + 3].isdigit() else parts[i + 3]
        result["Overall Risk"] = parts[i + 4]

        # --- Safeguards + Mitigated Risk Category ---
        j = i + 5
        while j < len(parts):
            if parts[j] in valid_risk_categories:
                result["Mitigated Risk Category"] = parts[j]
                break
            else:
                safeg.append(parts[j])
            j += 1
        result["Safeguards"] = "; ".join(safeg)

        # S/L/RR after safeguards + Overall Risk (mitigated)
        result["S"] = int(parts[j + 1]) if parts[j + 1].isdigit() else parts[j + 1]
        result["L"] = int(parts[j + 2]) if parts[j + 2].isdigit() else parts[j + 2]
        result["RR"] = int(parts[j + 3]) if parts[j + 3].isdigit() else parts[j + 3]
        result["Overall Risk"] = parts[j + 4]

        # --- Recommendations + final S/L/RR + Responsibility ---
        k = j + 5
        while k < len(parts) - 4:
            recomm.append(parts[k])
            k += 1
        result["Recommendations"] = "; ".join(recomm)

        result["S After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["L After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["RR After Recommendation"] = int(parts[k]) if parts[k].isdigit() else parts[k]; k += 1
        result["Responsibility"] = parts[k]

        # return as a list-of-rows for compatibility with rest of code
        return [[result[col] for col in headers]]

    # --- 2) Wrapper: use parse_llm_result for each line of the LLM output ---
    def parse_llm_result_to_rows(result_text: str) -> list[list[str]]:
        """
        Turns the whole LLM output (possibly multi-line) into list[list[str]]
        by calling parse_llm_result() on each non-empty line.
        """
        rows: list[list[str]] = []

        for line in str(result_text).strip().splitlines():
            if not line.strip():
                continue

            try:
                line_rows = parse_llm_result(line)
            except Exception:
                # Let caller log the malformed output; we just skip bad lines here
                continue

            # parse_llm_result already returns a list of rows; extend and
            # also defend against wrong length (just in case).
            for r in line_rows:
                if len(r) == len(headers):
                    rows.append(r)

        return rows

    query_infos = list_all_connections(pid_data)
    print(query_infos)
    valid_risk_categories = ["Low", "Medium", "High", "N/A"]
    
    headers = [
        "Node", "Guide Word", "Parameter", "Deviation", "Cause", "Consequence", 
        "Unmitigated Risk Category", "S Before Safeguards", "L Before Safeguards", 
        "RR Before Safeguards", "Overall Risk", "Safeguards", "Mitigated Risk Category", 
        "S", "L", "RR", "Overall Risk", "Recommendations", "S After Recommendation", 
        "L After Recommendation", "RR After Recommendation", "Responsibility"
    ]
    info_by_line: Dict[str, dict] = {info["line_id"]: info for info in query_infos}

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
    
    for sel in selections:
        line_id = sel.get("line_id")
        param = sel.get("parameter")
        guide_word = sel.get("guide_word")

        if not line_id or not param or not guide_word:
            continue

        info = info_by_line.get(line_id)
        if not info:
            logger.warning(f"[Skip] line_id {line_id} not found in pid_data")
            continue

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

                # ⬇️ per-selection parsing – NO global parsed_rows
                rows = parse_llm_result_to_rows(result)

                if not rows:
                    logger.warning(
                        f"[Warning] No valid rows for {info['line_id']}:{param}:{guide_word} "
                        f"(LLM output probably malformed CSV)"
                    )
                    error_entry = {
                        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "LineID": info["line_id"],
                        "Parameter": param,
                        "GuideWord": guide_word,
                        "RawOutput": result,
                        "Reason": f"Invalid or no rows parsed (expected {len(headers)} columns per row)"
                    }
                    error_df = pd.concat([error_df, pd.DataFrame([error_entry])], ignore_index=True)
                    error_df.to_csv(error_log_path, index=False)
                    continue

            except Exception as e:
                logger.error(f"[Error] {info['line_id']}:{param}:{guide_word} — {e}")
                continue

            if cb.total_tokens > token_limit:
                logger.warning(f"[Skipped] {line_id}:{param}:{guide_word} — {cb.total_tokens} tokens")
                continue

            tokens_used = cb.total_tokens

        # Log raw LLM output
        response_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "RawOutput": result,
        }
        llm_response_df = pd.concat([llm_response_df, pd.DataFrame([response_entry])], ignore_index=True)
        llm_response_df.to_csv(llm_response_log_path, index=False)

        # Build DataFrame ONLY from current selection's rows
        df_parsed = pd.DataFrame(rows, columns=headers)

        # --- merge into parsed_excel_path ---
        if os.path.exists(parsed_excel_path):
            df_existing = pd.read_excel(parsed_excel_path)
            df_existing = df_existing.loc[:, ~df_existing.columns.duplicated()]
            df_existing = df_existing.reindex(columns=headers)
            df_parsed = df_parsed.reindex(columns=headers)
            df_combined = pd.concat([df_existing, df_parsed], ignore_index=True)
        else:
            df_combined = df_parsed.reindex(columns=headers)

        df_combined.to_excel(parsed_excel_path, index=False)

        # --- main HAZOP output ---
        df = pd.concat([df, df_parsed], ignore_index=True)
        df.to_excel(excel_path, index=False)

        # token log
        token_row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "LineID": line_id,
            "Parameter": param,
            "GuideWord": guide_word,
            "Model": model_name,
            "PromptTokens": cb.prompt_tokens,
            "CompletionTokens": cb.completion_tokens,
            "TotalTokens": cb.total_tokens,
        }
        token_df = pd.concat([token_df, pd.DataFrame([token_row])], ignore_index=True)
        token_df.to_csv(token_log_path, index=False)

        yield f"{line_id}:{param}:{guide_word}", tokens_used