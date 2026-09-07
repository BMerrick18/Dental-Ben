from src.services.input_service import InputService
from src.modules.appointment.clinical_exam import Extra_oral, Intra_oral_ht, Intra_oral_st, Special_tests

def add_extra_oral():
    input_service = InputService()

    lymph_nodes = input_service.get_text("Lymph nodes: ")
    salivary_glands = input_service.get_text("Salivary glands: ")
    submandibular_zone = input_service.get_text("Submandibular zone: ")
    neck = input_service.get_text("Neck: ")
    tmj = input_service.get_text("TMJ: ")

    return Extra_oral(
        lymph_nodes=lymph_nodes,
        salivary_glands=salivary_glands,
        submandibular_zone=submandibular_zone,
        neck=neck,
        tmj=tmj)    

def add_intra_oral_st():
    input_service = InputService()

    palate = input_service.get_text("Palate: ")
    cheeks = input_service.get_text("Cheeks: ")
    lips = input_service.get_text("Lips: ")
    tongue = input_service.get_text("Tongue: ")
    gingiva = input_service.get_text("Gingiva: ")
    floor_of_mouth = input_service.get_text("Floor of mouth: ")

    return Intra_oral_st(
        palate=palate,
        cheeks=cheeks,
        lips=lips,
        tongue=tongue,
        gingiva=gingiva,
        floor_of_mouth=floor_of_mouth)
    
def add_intra_oral_ht():
    input_service = InputService()

    caries = input_service.comma_separated_to_list("Caries (comma-separated list): ")
    retained_roots = input_service.comma_separated_to_list("Retained roots (comma-separated list): ")
    fractures = input_service.comma_separated_to_list("Fractures (comma-separated list): ")
    recurrent_caries = input_service.comma_separated_to_list("Recurrent caries (comma-separated list): ")

    return Intra_oral_ht(
        caries=caries,
        retained_roots=retained_roots,
        fractures=fractures,
        recurrent_caries=recurrent_caries)

def add_special_tests():
    input_service = InputService()

    ttp = input_service.comma_separated_to_list("TTP (comma-separated list): ")
    endofrost = input_service.comma_separated_to_list("Endofrost (comma-separated list): ")

    return Special_tests(
        ttp=ttp,
        endofrost=endofrost)

if __name__ == "__main__":
    test_extra_oral = add_extra_oral()
    print(test_extra_oral.lymph_nodes, test_extra_oral.salivary_glands, test_extra_oral.submandibular_zone, test_extra_oral.neck, test_extra_oral.tmj)
    test_intra_oral_st = add_intra_oral_st()
    print(test_intra_oral_st.palate, test_intra_oral_st.cheeks, test_intra_oral_st.lips, test_intra_oral_st.tongue, test_intra_oral_st.gingiva, test_intra_oral_st.floor_of_mouth)
    test_intra_oral_ht = add_intra_oral_ht()
    print(test_intra_oral_ht.caries, test_intra_oral_ht.retained_roots, test_intra_oral_ht.fractures, test_intra_oral_ht.recurrent_caries)
    test_special_tests = add_special_tests()
    print(test_special_tests.ttp, test_special_tests.endofrost)


