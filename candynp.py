import os
import pandas as pd
import psr.factory as factory
from dataclasses import dataclass
import argparse


@dataclass
class LineCandidate:
    from_bus = ""
    to_bus = ""
    updated_nc = 0
    owner = ""
    resistance = 0
    reactance = 0
    susceptance = 0
    nominal_rating = 0
    emergency_rating = 0
    outage_prob = 0
    ref_cost = 0
    circuit_type = ""
    km = 0
    name = ""
    investment_cost = 0
    currency = 0
    o_m_cost = 0
    discount_rate = 0
    lifetime = 0
    belongs_to_the_study = 0
    dec_type = 0
    min_date_month = 1
    min_date_year = 2023
    max_date_month = 1
    max_date_year = 2200

    def to_list(self):
        return [self.from_bus, self.to_bus, self.updated_nc, self.owner, self.resistance, self.reactance,
                self.susceptance, self.nominal_rating, self.emergency_rating, self.outage_prob, self.ref_cost,
                self.circuit_type, self.km, self.name, self.investment_cost, self.currency, self.o_m_cost,
                self.discount_rate, self.lifetime, self.belongs_to_the_study, self.dec_type, self.min_date_month,
                self.min_date_year, self.max_date_month, self.max_date_year]


@dataclass
class TrafoCandidate:
    from_bus = ""
    to_bus = ""
    updated_nc = 0
    owner = ""
    resistance = 0
    reactance = 0
    min_tap = 0
    max_tap = 0
    min_angle = 0
    max_angle = 0
    control_type = ""
    controlled_bus = ""
    nominal_rating = 0
    emergency_rating = 0
    outage_prob = 0
    ref_cost = 0
    name = ""
    fixed_angle = 0
    min_limit_nominal_rating = 0
    max_limit_nominal_rating = 0
    min_limit_emergency_rating = 0
    max_limit_emergency_rating = 0
    investment_cost = 0
    currency = 0
    o_m_cost = 0
    discount_rate = 0
    lifetime = 0
    belongs_to_the_study = 0
    dec_type = 0
    min_date_month = 1
    min_date_year = 2023
    max_date_month = 1
    max_date_year = 2200

    def to_list(self):
        return [self.from_bus, self.to_bus, self.updated_nc, self.owner, self.resistance, self.reactance,
                self.min_tap, self.max_tap, self.min_angle, self.max_angle, self.control_type, self.controlled_bus,
                self.nominal_rating, self.emergency_rating, self.outage_prob, self.ref_cost, self.name,
                self.fixed_angle, self.min_limit_nominal_rating, self.max_limit_nominal_rating,
                self.min_limit_emergency_rating, self.max_limit_emergency_rating, self.investment_cost, self.currency,
                self.o_m_cost, self.discount_rate, self.lifetime, self.belongs_to_the_study, self.dec_type,
                self.min_date_month, self.min_date_year, self.max_date_month, self.max_date_year]


@dataclass
class Tr3wCandidate:
    primary_bus = ""
    secondary_bus = ""
    tertiary_bus = ""
    internal_bus_number = ""
    updated_nc = 0
    operation = ""
    resistance_primary_secondary = 0
    reactance_primary_secondary = 0
    resistance_secondary_tertiary = 0
    reactance_secondary_tertiary = 0
    resistance_primary_tertiary = 0
    reactance_primary_tertiary = 0
    outage_prob = 0
    ref_cost = 0
    date = ""
    condition = ""
    transformer_number = ""
    name = ""
    nominal_rating_primary = 0
    emergency_rating_primary = 0
    type_control_primary = ""
    fixed_angle_primary = 0
    min_angle_primary = 0
    max_angle_primary = 0
    min_limit_nominal_rating_primary = 0
    max_limit_nominal_rating_primary = 0
    min_limit_emergency_rating_primary = 0
    max_limit_emergency_rating_primary = 0
    min_tap_primary = 0
    max_tap_primary = 0
    steps_number_primary = 0
    controlled_bus_primary = ""
    nominal_rating_secondary = 0
    emergency_rating_secondary = 0
    type_control_secondary = ""
    fixed_angle_secondary = 0
    min_angle_secondary = 0
    max_angle_secondary = 0
    min_limit_nominal_rating_secondary = 0
    max_limit_nominal_rating_secondary = 0
    min_limit_emergency_rating_secondary = 0
    max_limit_emergency_rating_secondary = 0
    min_tap_secondary = 0
    max_tap_secondary = 0
    steps_number_secondary = 0
    controlled_bus_secondary = ""
    nominal_rating_terciary = 0
    emergency_rating_terciary = 0
    type_control_terciary = ""
    fixed_angle_terciary = 0
    min_angle_terciary = 0
    max_angle_terciary = 0
    min_limit_nominal_rating_terciary = 0
    max_limit_nominal_rating_terciary = 0
    min_limit_emergency_rating_terciary = 0
    max_limit_emergency_rating_terciary = 0
    min_tap_terciary = 0
    max_tap_terciary = 0
    steps_number_terciary = 0
    controlled_bus_terciary = ""
    investment_cost = 0
    currency = 0
    o_m_cost = 0
    discount_rate = 0
    lifetime = 0
    belongs_to_the_study = 0
    dec_type = 0
    min_date_month = 1
    min_date_year = 2023
    max_date_month = 1
    max_date_year = 2200

    def to_list(self):
        return [self.primary_bus, self.secondary_bus, self.tertiary_bus, self.internal_bus_number, self.updated_nc,
                self.operation, self.resistance_primary_secondary, self.reactance_primary_secondary,
                self.resistance_secondary_tertiary, self.reactance_secondary_tertiary, self.resistance_primary_tertiary,
                self.reactance_primary_tertiary, self.outage_prob, self.ref_cost, self.date, self.condition,
                self.transformer_number, self.name, self.nominal_rating_primary, self.emergency_rating_primary,
                self.type_control_primary, self.fixed_angle_primary, self.min_angle_primary, self.max_angle_primary,
                self.min_limit_nominal_rating_primary, self.max_limit_nominal_rating_primary,
                self.min_limit_emergency_rating_primary, self.max_limit_emergency_rating_primary, self.min_tap_primary,
                self.max_tap_primary, self.steps_number_primary, self.controlled_bus_primary,
                self.nominal_rating_secondary,
                self.emergency_rating_secondary, self.type_control_secondary, self.fixed_angle_secondary,
                self.min_angle_secondary, self.max_angle_secondary, self.min_limit_nominal_rating_secondary,
                self.max_limit_nominal_rating_secondary, self.min_limit_emergency_rating_secondary,
                self.max_limit_emergency_rating_secondary, self.min_tap_secondary, self.max_tap_secondary,
                self.steps_number_secondary, self.controlled_bus_secondary, self.nominal_rating_terciary,
                self.emergency_rating_terciary, self.type_control_terciary, self.fixed_angle_terciary,
                self.min_angle_terciary, self.max_angle_terciary, self.min_limit_nominal_rating_terciary,
                self.max_limit_nominal_rating_terciary, self.min_limit_emergency_rating_terciary,
                self.max_limit_emergency_rating_terciary, self.min_tap_terciary, self.max_tap_terciary,
                self.steps_number_terciary, self.controlled_bus_terciary, self.investment_cost, self.currency,
                self.o_m_cost, self.discount_rate, self.lifetime, self.belongs_to_the_study, self.dec_type,
                self.min_date_month, self.min_date_year, self.max_date_month, self.max_date_year]


def parallel_circuit_numbers(elements):
    nc_parallel = {}
    for element in elements:
        if element.get("FlagMonitored") == 1:
            key = (element.get("RefBuses")[0].code, element.get("RefBuses")[1].code)
            nc = element.get("Nc")
            if key in nc_parallel:
                nc_parallel[key] = max(nc_parallel[key], nc) + 1
            else:
                nc_parallel[key] = nc + 1
    return nc_parallel


def parallel_transformer_numbers_tr3w(tr3ws):
    nc_parallel = {}
    for tr3w in tr3ws:
        if any([tr3w.get("RefTransformers")[0].get("FlagMonitored"),
                tr3w.get("RefTransformers")[1].get("FlagMonitored"),
                tr3w.get("RefTransformers")[2].get("FlagMonitored")]):
            key = (tr3w.get("RefTransformers")[0].get("RefBuses")[0].code,
                   tr3w.get("RefTransformers")[1].get("RefBuses")[0].code,
                   tr3w.get("RefTransformers")[2].get("RefBuses")[0].code)
            nc = tr3w.get("Nc")
            if key in nc_parallel:
                nc_parallel[key] = max(nc_parallel[key], nc) + 1
            else:
                nc_parallel[key] = nc + 1
    return nc_parallel


def load_data(path):
    study = factory.load_study(path, "Netplan")
    usecir = pd.read_csv(os.path.join(path, "usecir.csv"), skiprows=3)
    return study, usecir


def generate_candidates(study, usecir, max_use):
    circuits = list(study.find("Circuit.*"))
    nc_parallel = parallel_circuit_numbers(circuits)
    line_candidates = []
    for circuit in circuits:
        if circuit.get("FlagMonitored") == 1:
            max_circ_use = usecir[circuit.name].max()
            if max_circ_use > max_use:
                print(f"{circuit.name}: {max_circ_use}")
                key = (circuit.get("RefBuses")[0].code, circuit.get("RefBuses")[1].code)
                number_candidates = max(0, int(max_circ_use / max_use) - 1)
                for i in range(number_candidates + 1):
                    line_candidate = LineCandidate()
                    line_candidate.from_bus = circuit.get("RefBuses")[0].code
                    line_candidate.to_bus = circuit.get("RefBuses")[1].code
                    line_candidate.updated_nc = nc_parallel[key] + i
                    nc_parallel[key] += 1
                    line_candidate.owner = circuit.get("O")
                    line_candidate.resistance = circuit.get("R")
                    line_candidate.reactance = circuit.get("X")
                    line_candidate.susceptance = circuit.get("MVAr")
                    line_candidate.nominal_rating = circuit.get("Rn")
                    line_candidate.emergency_rating = circuit.get("Re")
                    line_candidate.outage_prob = circuit.get("Prob")
                    line_candidate.ref_cost = circuit.get("Cost")
                    line_candidate.circuit_type = circuit.get("Type")
                    line_candidate.km = circuit.get("Km")
                    line_candidate.name = ""
                    line_candidate.investment_cost = circuit.get("Cost")
                    line_candidates.append(line_candidate)

    header = ["$From bus", "To bus", "Circuit number", "Owner", "Resistance", "Reactance", "Susceptance",
              "Nominal rating",
              "Emergency rating", "Outage prob.", "Ref. cost", "Circuit type", "(..Km..)", "(........Name..........)",
              "Investment cost", "Currency", "O&M cost", "Discount rate", "Lifetime", "Belongs to the study",
              "dec_type",
              "min_date", "min_date", "max_date", "max_date"]
    df = pd.DataFrame([line_candidate.to_list() for line_candidate in line_candidates], columns=header)
    df.to_csv("dlad_candidates.csv", index=False)

    print(f"File 'dlad_candidates.csv' created with {len(line_candidates)} entries.")

    transformers = list(study.find("Transformer.*"))
    nc_parallel = parallel_circuit_numbers(transformers)
    trafo_candidates = []

    for transformer in transformers:
        if transformer.get("FlagMonitored") == 1:
            max_circ_use = usecir[transformer.name].max() if transformer.name in usecir else 0
            if max_circ_use > max_use:
                print(f"{transformer.name}: {max_circ_use}")
                number_candidates = max(0, int(max_circ_use / max_use))
                key = (transformer.get("RefBuses")[0].code, transformer.get("RefBuses")[1].code)
                for i in range(number_candidates):
                    trafo_candidate = TrafoCandidate()
                    trafo_candidate.from_bus = transformer.get("RefBuses")[0].code
                    trafo_candidate.to_bus = transformer.get("RefBuses")[1].code
                    trafo_candidate.updated_nc = nc_parallel[key] + i
                    nc_parallel[key] += 1
                    trafo_candidate.owner = transformer.get("O")
                    trafo_candidate.resistance = transformer.get("R")
                    trafo_candidate.reactance = transformer.get("X")
                    trafo_candidate.min_tap = transformer.get("Tmn")
                    trafo_candidate.max_tap = transformer.get("Tmx")
                    trafo_candidate.min_angle = transformer.get("Pmn")
                    trafo_candidate.max_angle = transformer.get("Pmx")
                    trafo_candidate.control_type = transformer.get("ControlType")
                    trafo_candidate.controlled_bus = transformer.get("RefBuses")[0].code
                    trafo_candidate.nominal_rating = transformer.get("Rn")
                    trafo_candidate.emergency_rating = transformer.get("Re")
                    trafo_candidate.outage_prob = transformer.get("Prob")
                    trafo_candidate.ref_cost = transformer.get("Cost")
                    trafo_candidate.name = ""
                    trafo_candidate.investment_cost = transformer.get("Cost")
                    trafo_candidates.append(trafo_candidate)

    header = ["$From bus", "To bus", "Circuit number", "Owner", "Resistance", "Reactance", "Min. tap", "Max. tap",
              "Min. angle", "Max. angle", "Control type", "Controlled bus", "Nominal rating", "Emergency rating",
              "Outage prob.", "Ref. cost", "(........Name..........)", "Fixed angle", "Min. limit of nominal rating",
              "Max limit of nominal rating", "Min limit of emergency rating", "Max limit of emergency rating",
              "Investment cost", "Currency", "O&M cost", "Discount rate", "Lifetime", "Belongs to the study",
              "dec_type",
              "min_date", "min_date", "max_date", "max_date"]

    df = pd.DataFrame([trafo_candidate.to_list() for trafo_candidate in trafo_candidates], columns=header)
    df.to_csv("dtad_candidates.csv", index=False)

    print(f"File 'dtad_candidates.csv' created with {len(trafo_candidates)} entries.")

    tr3ws = list(study.find("ThreeWindingsTransformer.*"))
    nc_parallel = parallel_transformer_numbers_tr3w(tr3ws)
    tr3w_candidates = []
    for tr3w in tr3ws:
        if any([tr3w.get("RefTransformers")[0].get("FlagMonitored"),
                tr3w.get("RefTransformers")[1].get("FlagMonitored"),
                tr3w.get("RefTransformers")[2].get("FlagMonitored")]):
            max_circ_use = max(usecir[tr3w.get("RefTransformers")[0].name].max(),
                               usecir[tr3w.get("RefTransformers")[1].name].max(),
                               usecir[tr3w.get("RefTransformers")[2].name].max()) \
                if (tr3w.get("RefTransformers")[0].name in usecir and
                    tr3w.get("RefTransformers")[1].name in usecir and
                    tr3w.get("RefTransformers")[2].name in usecir) \
                else 0
            key = (tr3w.get("RefTransformers")[0].get("RefBuses")[0].code,
                   tr3w.get("RefTransformers")[1].get("RefBuses")[0].code,
                   tr3w.get("RefTransformers")[2].get("RefBuses")[0].code)
            print(f"{key}: {max_circ_use}")
            if max_circ_use > max_use:
                number_candidates = max(0, int(max_circ_use / max_use))
                for i in range(number_candidates):
                    tr3w_candidate = Tr3wCandidate()
                    tr3w_candidate.primary_bus = tr3w.get("RefTransformers")[0].get("RefBuses")[0].code
                    tr3w_candidate.secondary_bus = tr3w.get("RefTransformers")[1].get("RefBuses")[0].code
                    tr3w_candidate.tertiary_bus = tr3w.get("RefTransformers")[2].get("RefBuses")[0].code
                    tr3w_candidate.internal_bus_number = ""
                    tr3w_candidate.updated_nc = nc_parallel[key] + i
                    tr3w_candidate.operation = tr3w.get("O")
                    tr3w_candidate.resistance_primary_secondary = tr3w.get("RPS")
                    tr3w_candidate.reactance_primary_secondary = tr3w.get("XPS")
                    tr3w_candidate.resistance_secondary_tertiary = tr3w.get("RST")
                    tr3w_candidate.reactance_secondary_tertiary = tr3w.get("XST")
                    tr3w_candidate.resistance_primary_tertiary = tr3w.get("RPT")
                    tr3w_candidate.reactance_primary_tertiary = tr3w.get("XPT")
                    tr3w_candidate.nominal_rating_primary = tr3w.get("RefTransformers")[0].get("Rn")
                    tr3w_candidate.emergency_rating_primary = tr3w.get("RefTransformers")[0].get("Re")
                    tr3w_candidate.type_control_primary = tr3w.get("RefTransformers")[0].get("ControlType")
                    tr3w_candidate.fixed_angle_primary = tr3w.get("RefTransformers")[0].get("Pmn")
                    tr3w_candidate.min_angle_primary = tr3w.get("RefTransformers")[0].get("Pmn")
                    tr3w_candidate.max_angle_primary = tr3w.get("RefTransformers")[0].get("Pmx")
                    tr3w_candidate.min_limit_nominal_rating_primary = tr3w.get("RefTransformers")[0].get("Rn")
                    tr3w_candidate.max_limit_nominal_rating_primary = tr3w.get("RefTransformers")[0].get("Rn")
                    tr3w_candidate.min_limit_emergency_rating_primary = tr3w.get("RefTransformers")[0].get("Re")
                    tr3w_candidate.max_limit_emergency_rating_primary = tr3w.get("RefTransformers")[0].get("Re")
                    tr3w_candidate.min_tap_primary = tr3w.get("RefTransformers")[0].get("Tmn")
                    tr3w_candidate.max_tap_primary = tr3w.get("RefTransformers")[0].get("Tmx")
                    tr3w_candidate.controlled_bus_primary = tr3w.get("RefTransformers")[0].get("RefBuses")[0].code
                    tr3w_candidate.nominal_rating_secondary = tr3w.get("RefTransformers")[1].get("Rn")
                    tr3w_candidate.emergency_rating_secondary = tr3w.get("RefTransformers")[1].get("Re")
                    tr3w_candidate.type_control_secondary = tr3w.get("RefTransformers")[1].get("ControlType")
                    tr3w_candidate.fixed_angle_secondary = tr3w.get("RefTransformers")[1].get("Pmn")
                    tr3w_candidate.min_angle_secondary = tr3w.get("RefTransformers")[1].get("Pmn")
                    tr3w_candidate.max_angle_secondary = tr3w.get("RefTransformers")[1].get("Pmx")
                    tr3w_candidate.min_limit_nominal_rating_secondary = tr3w.get("RefTransformers")[1].get("Rn")
                    tr3w_candidate.max_limit_nominal_rating_secondary = tr3w.get("RefTransformers")[1].get("Rn")
                    tr3w_candidate.min_limit_emergency_rating_secondary = tr3w.get("RefTransformers")[1].get("Re")
                    tr3w_candidate.max_limit_emergency_rating_secondary = tr3w.get("RefTransformers")[1].get("Re")
                    tr3w_candidate.min_tap_secondary = tr3w.get("RefTransformers")[1].get("Tmn")
                    tr3w_candidate.max_tap_secondary = tr3w.get("RefTransformers")[1].get("Tmx")
                    tr3w_candidate.controlled_bus_secondary = tr3w.get("RefTransformers")[1].get("RefBuses")[0].code
                    tr3w_candidate.nominal_rating_terciary = tr3w.get("RefTransformers")[2].get("Rn")
                    tr3w_candidate.emergency_rating_terciary = tr3w.get("RefTransformers")[2].get("Re")
                    tr3w_candidate.type_control_terciary = tr3w.get("RefTransformers")[2].get("ControlType")
                    tr3w_candidate.fixed_angle_terciary = tr3w.get("RefTransformers")[2].get("Pmn")
                    tr3w_candidate.min_angle_terciary = tr3w.get("RefTransformers")[2].get("Pmn")
                    tr3w_candidate.max_angle_terciary = tr3w.get("RefTransformers")[2].get("Pmx")
                    tr3w_candidate.min_limit_nominal_rating_terciary = tr3w.get("RefTransformers")[2].get("Rn")
                    tr3w_candidate.max_limit_nominal_rating_terciary = tr3w.get("RefTransformers")[2].get("Rn")
                    tr3w_candidate.min_limit_emergency_rating_terciary = tr3w.get("RefTransformers")[2].get("Re")
                    tr3w_candidate.max_limit_emergency_rating_terciary = tr3w.get("RefTransformers")[2].get("Re")
                    tr3w_candidate.min_tap_terciary = tr3w.get("RefTransformers")[2].get("Tmn")
                    tr3w_candidate.max_tap_terciary = tr3w.get("RefTransformers")[2].get("Tmx")
                    tr3w_candidate.controlled_bus_terciary = tr3w.get("RefTransformers")[2].get("RefBuses")[0].code
                    tr3w_candidate.investment_cost = tr3w.get("Cost")
                    tr3w_candidates.append(tr3w_candidate)

    header = ["$Primary bus", "Secondary bus", "Tertiary bus", "Internal bus number", "Circuit number", "Operation",
              "Resistance primary-secondary", "Reactance primary-secondary", "Resistance secondary-tertiary",
              "Reactance secondary-tertiary", "Resistance primary-tertiary", "Reactance primary-tertiary",
              "Outage prob.",
              "Ref. cost", "(..Date..)", "Condition", "Transformer number", "(.........Name.........)",
              "Nominal rating",
              "Emergency rating", "Type control", "Fixed angle", "Min. angle", "Max. angle",
              "Min limit of nominal rating",
              "Max limit of nominal rating", "Min limit of emergency rating", "Max limit of emergency rating",
              "Min tap",
              "Max tap", "Steps number", "Controlled bus", "Nominal rating", "Emergency rating", "Type control",
              "Fixed angle", "Min. angle", "Max. angle", "Min limit of nominal rating", "Max limit of nominal rating",
              "Min limit of emergency rating", "Max limit of emergency rating", "Min tap", "Max tap", "Steps number",
              "Controlled bus", "Nominal rating", "Emergency rating", "Type control", "Fixed angle", "Min. angle",
              "Max. angle", "Min limit of nominal rating", "Max limit of nominal rating",
              "Min limit of emergency rating",
              "Max limit of emergency rating", "Min tap", "Max tap", "Steps number", "Controlled bus",
              "Investment cost",
              "Currency", "O&M cost", "Discount rate", "Lifetime", "Belongs to the study", "dec_type", "min_date",
              "min_date", "max_date", "max_date"]

    df = pd.DataFrame([tr3w_candidate.to_list() for tr3w_candidate in tr3w_candidates], columns=header)
    df.to_csv("dt3ad_candidates.csv", index=False)

    print(f"File 'dt3ad_candidates.csv' created with {len(tr3w_candidates)} entries.")


def main():
    parser = argparse.ArgumentParser(description="Generate candidates for Network Expansion Planning")
    parser.add_argument("max_use", type=int, default=80, help="Maximum usage threshold")
    parser.add_argument("path", type=str, help="Path to the case directory")

    args = parser.parse_args()

    study, usecir = load_data(args.path)
    generate_candidates(study, usecir, args.max_use)


if __name__ == "__main__":
    main()