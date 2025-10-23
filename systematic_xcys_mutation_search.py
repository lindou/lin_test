#!/usr/bin/env python3
"""
Systematic Search: X→C Mutations in Proteins with Nanobody Structures

This script catalogs all oncologic proteins that have:
1. Nanobody co-crystal structure (PDB available)
2. X→C mutations (any residue mutating TO cysteine)
3. Clinical/cancer relevance
"""

# List of proteins with confirmed nanobody structures
proteins_with_nanobodies = {
    "EGFR": {
        "pdb_codes": ["4KRL", "4KRN", "5JTB", "6S8C"],
        "extracellular_domain": "1-621",
        "cancer_types": ["NSCLC", "glioblastoma", "colorectal"],
        "known_mutations": {
            "common": ["L858R", "T790M", "exon19del"],
            "need_to_check_for_XtoC": True
        }
    },
    
    "HER2/ERBB2": {
        "pdb_codes": ["5MY6", "6OGE"],
        "extracellular_domain": "1-652",
        "cancer_types": ["breast", "gastric", "ovarian"],
        "known_mutations": {
            "common": ["S310F", "L755S"],
            "XtoC_status": "Previously checked - no significant ones found"
        }
    },
    
    "MET": {
        "pdb_codes": ["Unknown - need to verify"],
        "extracellular_domain": "1-932 (Sema-PSI-IPT)",
        "cancer_types": ["NSCLC", "gastric", "renal"],
        "known_mutations": {
            "common": ["exon14 skipping", "Y1230C (kinase domain - intracellular)"],
            "need_to_check_for_XtoC": True
        }
    },
    
    "FGFR3": {
        "pdb_codes": ["None with nanobody - structure alone: 4K33"],
        "extracellular_domain": "1-375",
        "cancer_types": ["bladder", "multiple myeloma"],
        "known_mutations": {
            "XtoC_confirmed": ["S249C", "R248C", "G370C", "S371C", "Y373C"],
            "frequency": "60-75% of low-grade bladder cancer",
            "status": "BEST TARGET but NO NANOBODY"
        }
    },
    
    "RET": {
        "pdb_codes": ["None with nanobody found"],
        "extracellular_domain": "1-636",
        "cancer_types": ["MTC", "MEN2", "NSCLC (fusions)"],
        "known_mutations": {
            "XtoC_type": "Cys→X (removes cysteine, creates unpaired)",
            "mutations": ["C634W", "C618F", "C620F"],
            "status": "Creates UNPAIRED cysteines (reactive!)"
        }
    },
    
    "PD-L1/CD274": {
        "pdb_codes": ["Multiple reported, need specific codes"],
        "extracellular_domain": "entire protein (small, ~290aa)",
        "cancer_types": ["melanoma", "NSCLC", "bladder", "others"],
        "known_mutations": {
            "frequency": "Rare - PD-L1 typically overexpressed, not mutated",
            "need_to_check_for_XtoC": True
        }
    },
    
    "PD-1/PDCD1": {
        "pdb_codes": ["Check if nanobody exists"],
        "extracellular_domain": "entire protein",
        "cancer_types": ["various"],
        "known_mutations": {
            "frequency": "Very rare",
            "need_to_check_for_XtoC": True
        }
    },
    
    "CTLA-4": {
        "pdb_codes": ["Check if nanobody exists"],
        "extracellular_domain": "entire protein",
        "cancer_types": ["melanoma", "others"],
        "known_mutations": {
            "frequency": "Rare",
            "need_to_check_for_XtoC": True
        }
    },
    
    "Integrins_ITGAV": {
        "pdb_codes": ["Check for αVβ3 nanobody"],
        "extracellular_domain": "entire protein (extracellular)",
        "cancer_types": ["metastatic cancers", "angiogenesis"],
        "known_mutations": {
            "need_to_check_for_XtoC": True
        }
    },
    
    "CDH1_Ecadherin": {
        "pdb_codes": ["Check if nanobody exists"],
        "extracellular_domain": "1-700 (cadherin repeats)",
        "cancer_types": ["gastric", "lobular breast"],
        "known_mutations": {
            "common": "Loss of function mutations",
            "need_to_check_for_XtoC": True
        }
    },
    
    "VEGFA": {
        "pdb_codes": ["Anti-VEGF nanobody structures exist"],
        "extracellular_domain": "secreted protein",
        "cancer_types": ["angiogenesis in all cancers"],
        "known_mutations": {
            "frequency": "Rare",
            "need_to_check_for_XtoC": True
        }
    }
}

# Summary of what needs to be checked
print("=" * 80)
print("PROTEINS WITH NANOBODY STRUCTURES: X→C MUTATION STATUS")
print("=" * 80)

confirmed_XtoC = []
needs_checking = []
no_nanobody = []

for protein, data in proteins_with_nanobodies.items():
    print(f"\n{protein}:")
    print(f"  PDB: {', '.join(data['pdb_codes'])}")
    print(f"  Extracellular domain: {data['extracellular_domain']}")
    print(f"  Cancer relevance: {', '.join(data['cancer_types'])}")
    
    if "XtoC_confirmed" in data["known_mutations"]:
        print(f"  ✅ CONFIRMED X→C mutations: {data['known_mutations']['XtoC_confirmed']}")
        confirmed_XtoC.append(protein)
    elif "None" in data['pdb_codes'][0] or "Unknown" in data['pdb_codes'][0]:
        print(f"  ❌ NO NANOBODY STRUCTURE")
        no_nanobody.append(protein)
    elif data["known_mutations"].get("need_to_check_for_XtoC"):
        print(f"  ⚠️  NEEDS COSMIC DATABASE SEARCH for X→C mutations")
        needs_checking.append(protein)
    else:
        print(f"  Status: {data['known_mutations']}")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
print(f"\n✅ Confirmed X→C mutations (but NO nanobody):")
for p in confirmed_XtoC:
    print(f"   - {p}")

print(f"\n⚠️  Has nanobody, NEEDS X→C mutation check:")
for p in needs_checking:
    print(f"   - {p}")

print(f"\n❌ Has X→C mutations but NO nanobody:")
for p in no_nanobody:
    print(f"   - {p}")

print("\n" + "=" * 80)
print("NEXT ACTION: Search COSMIC database for X→C mutations in:")
print("=" * 80)
for p in needs_checking:
    print(f"  - {p}")
