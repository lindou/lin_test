# DETAILED X→C MUTATION ANALYSIS
## Oncologic Proteins with Nanobody Structures

---

## 🎯 PRIORITY 1: EGFR (HIGH CONFIDENCE)

### Nanobody Structures Available:
- **PDB 4KRL, 4KRN:** EGFR-ECD with nanobodies EgB1, EgB4
- **PDB 5JTB:** EGFR with nanobody 7D12
- **PDB 6S8C:** More recent structure

### Target Region:
- **Extracellular domain:** aa 1-621 (Domains I, II, III, IV)

### Known EGFR Mutations:
**Most common (kinase domain - NOT useful):**
- L858R (exon 21) - intracellular ❌
- Exon 19 deletions - intracellular ❌
- T790M (resistance) - intracellular ❌

**Extracellular mutations (less common):**
- **EGFRvIII** (Δexon 2-7) - deletion, not X→C ❌
- Need to search COSMIC for **rare X→C in aa 1-621**

### COSMIC Search Parameters:
```
Gene: EGFR
Position: 1-621
Mutation type: Substitution - Missense
Pattern: p.*###C (any amino acid → Cysteine)
Cancer types: NSCLC, glioblastoma, colorectal
Minimum frequency: >0.5%
```

### Expected Outcome:
- **Probability of finding X→C:** 20-30%
- EGFR is heavily mutated, may have rare extracellular X→C

---

## 🎯 PRIORITY 2: PD-L1/CD274 (IMMUNOTHERAPY RELEVANCE)

### Nanobody Status:
- **Multiple papers mention PD-L1 nanobodies**
- Specific PDB codes need verification
- Likely available (therapeutic target)

### Target Region:
- **Entire protein:** Small extracellular protein (~290 aa)

### Known PD-L1 Biology:
- **Mechanism:** Typically OVEREXPRESSED, not mutated
- **Mutations:** Very rare in cancer
- Most therapeutic strategies involve blockade, not mutation targeting

### COSMIC Search:
```
Gene: CD274
Position: All (1-290)
Pattern: p.*###C
Minimum frequency: >0.1% (lower threshold due to rarity)
```

### Expected Outcome:
- **Probability of X→C:** 5-10% (mutations are rare)
- If found, would be HIGH impact (immunotherapy context)

---

## 🎯 PRIORITY 3: CDH1 (E-cadherin) (GASTRIC/BREAST CANCER)

### Nanobody Status:
- **Need to verify** if cadherin nanobodies exist
- E-cadherin is therapeutic target, nanobodies likely

### Target Region:
- **Extracellular:** Cadherin repeats (aa 1-700)

### Known CDH1 Mutations:
- **Very common in gastric cancer** (~50% of diffuse gastric)
- **Also in lobular breast cancer** (~60%)
- Most mutations are **loss-of-function** (truncations, frameshift)

### Key Question:
- Do X→C **gain-of-function** mutations exist?
- Or are all mutations inactivating?

### COSMIC Search:
```
Gene: CDH1
Position: 1-700 (extracellular repeats)
Pattern: p.*###C
Cancer types: Gastric (diffuse type), lobular breast
Frequency: >1%
```

### Expected Outcome:
- **Probability:** 10-20%
- CDH1 is heavily mutated, but mostly loss-of-function
- X→C might be rare

---

## 🎯 PRIORITY 4: Integrins (αVβ3, α5β1) (METASTASIS)

### Nanobody Status:
- **RGD-binding integrin nanobodies exist**
- Used for imaging/targeting
- Need PDB codes

### Target Region:
- **αV (ITGAV):** Extracellular domain
- **β3 (ITGB3):** Extracellular domain

### Known Integrin Mutations:
- **Less studied than RTKs**
- Some germline mutations in thrombosis
- Somatic cancer mutations underexplored

### COSMIC Search:
```
Gene: ITGAV, ITGB3, ITGA5, ITGB1
Position: Extracellular domains
Pattern: p.*###C
Cancer types: All (metastasis-related)
```

### Expected Outcome:
- **Probability:** 10-15%
- Worth checking, but less likely than RTKs

---

## 🎯 PRIORITY 5: VEGF-A (ANGIOGENESIS)

### Nanobody Status:
- **Anti-VEGF nanobodies exist**
- Used therapeutically (e.g., caplacizumab targets VWF, similar approach)

### Target Region:
- **Secreted protein:** ~190 aa

### Known VEGF Mutations:
- **Very rare** - VEGF typically overexpressed
- Mutations in VEGF receptors more common

### Expected Outcome:
- **Probability of X→C:** <5%
- Low priority

---

## 🎯 PRIORITY 6: PD-1, CTLA-4 (LOW PRIORITY)

### Why Low Priority:
- **Germline proteins** - mutations extremely rare
- Therapeutic targets via blockade, not mutation-specific
- Unlikely to find X→C mutations

---

## 📊 SUMMARY TABLE: Likelihood of Finding X→C Mutations

| Protein | Nanobody PDB | X→C Probability | Market Size | Overall Score |
|---------|--------------|-----------------|-------------|---------------|
| **EGFR** | ✅ 4KRL, 5JTB | 20-30% | ⭐⭐⭐⭐⭐ | **⭐⭐⭐⭐⭐** |
| **CDH1** | ⚠️ Check | 10-20% | ⭐⭐⭐⭐ | **⭐⭐⭐⭐** |
| **PD-L1** | ⚠️ Likely | 5-10% | ⭐⭐⭐⭐⭐ | **⭐⭐⭐** |
| **Integrins** | ⚠️ Check | 10-15% | ⭐⭐⭐ | **⭐⭐⭐** |
| **VEGF-A** | ✅ Yes | <5% | ⭐⭐⭐⭐ | **⭐⭐** |
| **PD-1** | ⚠️ Check | <5% | ⭐⭐⭐⭐⭐ | **⭐** |
| **CTLA-4** | ⚠️ Check | <5% | ⭐⭐⭐⭐ | **⭐** |

---

## 🔥 TOP RECOMMENDATION: **EGFR**

### Why EGFR is Your Best Bet:

1. ✅ **Nanobody structures exist** (4KRL, 5JTB) - can start immediately
2. ✅ **EGFR is heavily mutated** - 20-30% chance of finding extracellular X→C
3. ✅ **Huge market** - NSCLC, glioblastoma
4. ✅ **Extracellular domain accessible** (aa 1-621)
5. ✅ **Clinical validation** - EGFR inhibitors already approved

### Immediate Action for EGFR:

**STEP 1: Search COSMIC Database**
1. Go to: https://cancer.sanger.ac.uk/cosmic/gene/analysis?ln=EGFR
2. Click "Mutations" → "Genome screen"
3. Filter:
   - Position: 1-621 (extracellular)
   - Mutation: Substitution
   - Look for pattern ending in "C" (cysteine)
4. Check frequencies in NSCLC, glioblastoma

**STEP 2: If X→C Found:**
1. Download PDB 4KRL or 5JTB
2. Locate mutation position in structure
3. Measure distance from nanobody CDR loops to mutation
4. If < 20 Å → **YOU HAVE YOUR TARGET!**

**STEP 3: Alternative Literature Search:**
Search PubMed for:
- "EGFR extracellular domain mutation cysteine"
- "EGFR ectodomain mutation cancer"
- May find published mutations not in COSMIC

---

## 💡 BACKUP PLAN: CDH1 (E-cadherin)

### If EGFR doesn't pan out:

**CDH1 advantages:**
- Very common in gastric cancer (50%)
- Also lobular breast cancer
- Extracellular cadherin repeats accessible

**Action:**
1. Verify if cadherin nanobodies exist
2. Search COSMIC for CDH1 X→C in aa 1-700
3. Focus on gastric cancer, lobular breast

---

## ⚠️ REALITY CHECK:

### Most Likely Outcome:

**Scenario A (60% probability):**
- No abundant X→C mutations in EGFR extracellular domain
- Most cancer-driving mutations are in kinase domain (intracellular)
- **Conclusion:** Accept that FGFR3 is best target, generate nanobody

**Scenario B (30% probability):**
- Find rare EGFR extracellular X→C mutation (<1% frequency)
- Low frequency = small market, but publishable proof-of-concept
- **Conclusion:** Proceed with EGFR, demonstrate platform

**Scenario C (10% probability):**
- **JACKPOT:** Find EGFR extracellular X→C with >1% frequency
- **Conclusion:** This is your ideal target!

---

## 🎯 NEXT STEPS (THIS WEEK):

### Day 1-2: COSMIC Search
1. Search EGFR (aa 1-621) for X→C mutations
2. Search CDH1 (aa 1-700) for X→C mutations
3. Search PD-L1 for X→C mutations

### Day 3: Structure Verification
1. Download PDB 4KRL (EGFR-nanobody)
2. Download PDB 5MY6 (HER2-nanobody, backup)
3. Familiarize with structures

### Day 4-5: Decision Point
**IF X→C found in EGFR/CDH1:**
- Analyze structure
- Calculate distances
- Design warhead strategy
- **GO!**

**IF NO X→C found:**
- Accept FGFR3 as best target
- Plan nanobody generation (6-12 months)
- Budget $50-100K

---

## 📝 MANUAL COSMIC SEARCH GUIDE:

### Step-by-Step for EGFR:

1. **Go to COSMIC:** https://cancer.sanger.ac.uk/cosmic
2. **Search gene:** Enter "EGFR" in search box
3. **Navigate to mutations:** Click "Mutations" tab
4. **Filter by position:**
   - Click "Add filter"
   - Select "AA position"
   - Enter: 1-621
5. **Filter by mutation type:**
   - Select "Substitution - Missense"
6. **Look for pattern:**
   - Sort by "AA mutation"
   - Look for entries ending in "C" (e.g., p.L23C, p.S45C)
7. **Check frequency:**
   - Look at "Sample count" column
   - Calculate: (sample count / total samples) × 100%
8. **Note cancer types:**
   - Check which cancers have the mutation
   - Prioritize NSCLC, glioblastoma

### Repeat for:
- CDH1 (positions 1-700)
- CD274/PD-L1 (all positions)
- ITGAV/integrins

