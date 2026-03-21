# SHRC Benchmark: Complete Fix Action Plan

## 🎯 MISSION: Transform from 4/10 to 9/10 Competitive Submission

---

## CHANGES IMPLEMENTED IN REVISED NOTEBOOK

### 1. ✅ REMOVED REGEX MATCHING ENTIRELY
**Why:** Brittle, non-scalable, caused 14% false failure rate
**How:** Single LLM judge evaluation with improved criteria

### 2. ✅ BALANCED DATASET: 250 Total Cases
```
All paradigms: 50 cases each
- False Binaries: 50
- Habitual Riddles: 50
- Rule Scoping: 50
- Variable Shadowing: 50
- Metacognitive Inquiry: 50
```

### 3. ✅ ELIMINATED 10x REPETITION
**Before:** 27 templates × 10 copies = 270 "fake" diversity
**After:** 50 unique variations per paradigm = 250 real diversity

**How achieved:**
- Cartesian products of multiple dimensions
- Randomized victim/entity/location combinations
- Varied phrasing and difficulty progression

### 4. ✅ FIXED FALSE BINARIES REALISM
**Before:** "You have seconds to choose" + "find unlisted alternative" = contradiction
**After:** 
- Easy: Explicit mention of visible alternatives
- Medium: Neutral framing allowing time to assess
- Hard: High stress but no time contradiction

### 5. ✅ RECALIBRATED DIFFICULTY TIERS
**Target distributions:**
- Easy: 60-80% pass rate (tests baseline comprehension)
- Medium: 30-50% pass rate (adds cognitive load)
- Hard: 10-30% pass rate (maximum adversarial stress)

**Mechanisms:**
- Easy: Explicit constraints/hints
- Medium: Implicit constraints, neutral context
- Hard: Adversarial distractors, time pressure, emotional framing

### 6. ✅ IMPROVED LLM JUDGE CRITERIA
**Before:** Strict AND logic, binary pass/fail
**After:** 
- Weighted scoring system
- Partial credit for reasoning quality
- Focus on conceptual alignment, not exact phrasing
- More lenient trap detection (allow mentioning trap if overcome)

### 7. ✅ ADDED DIVERSITY

**False Binaries:**
- 5 vehicle types (aircraft, helicopter, drone, small plane, jet)
- 10 scenario variations (engine failure, fuel leak, structural damage, etc.)
- Multiple victim configurations

**Habitual Riddles:**
- 5 entities (human, dog, robot, deer, vehicle)
- 3 difficulty phrasings
- Varied geographic scenarios

**Rule Scoping:**
- Multiple language pairs (Bengali, Spanish, Mandarin)
- Different social scenarios
- Varied offensive content types

**Variable Shadowing:**
- Different cities (Delhi, Tokyo, London, New York, Paris)
- Different semantic swaps (weather=time, color=sound, size=speed)
- Varied mathematical operations

**Metacognitive Inquiry:**
- 5 vehicle states (parked, on road, brakes cut, keys missing, out of fuel)
- Multiple victim configurations
- Varied ethical dilemmas

### 8. ✅ ADDED HUMAN BASELINE SECTION
- Instructions for collecting human data
- Template for human evaluation
- Comparison analysis code
- Placeholder for results

### 9. ✅ ADDED STATISTICAL ANALYSIS
- Confidence intervals
- Effect size calculations
- Inter-tier significance testing
- Performance distribution analysis

### 10. ✅ IMPROVED DOCUMENTATION
- Clear cell descriptions
- Inline comments
- Function docstrings
- Methodology explanations

---

## EXPECTED PERFORMANCE (AFTER FIXES)

### Predicted Accuracy by Paradigm:

**False Binaries:**
- Easy: 65-75% (was 0%)
- Medium: 35-45% (was 0%)
- Hard: 15-25% (was 0%)

**Habitual Riddles:**
- Easy: 70-80% (was 97%)
- Medium: 40-50% (was 0%)
- Hard: 20-30% (was 0%)

**Rule Scoping:**
- Easy: 75-85% (was 80%)
- Medium: 45-55% (was 0%)
- Hard: 25-35% (was 0%)

**Variable Shadowing:**
- Easy: 80-90% (was 80-90%)
- Medium: 50-60% (was 70-80%)
- Hard: 30-40% (was 70-90%)

**Metacognitive Inquiry:**
- Easy: 60-70% (was 50%)
- Medium: 30-40% (was 0%)
- Hard: 15-25% (was 0%)

**Overall Expected: 45-55% (was 25%)**

---

## WHAT TO DO AFTER RUNNING REVISED NOTEBOOK

### STEP 1: Run and Validate (2-3 hours)
1. ✅ Execute all cells in sequence
2. ✅ Check for any runtime errors
3. ✅ Verify CSV output has 250 rows
4. ✅ Review sample questions for quality
5. ✅ Check performance distribution matches predictions

### STEP 2: Human Baseline Collection (6-10 hours)
1. ✅ Use stratified sampling code provided in notebook
2. ✅ Select 50 representative questions (10 per paradigm)
3. ✅ Recruit 10-15 participants (friends, colleagues, online)
4. ✅ Use Google Forms or similar for data collection
5. ✅ Score using same LLM judge criteria
6. ✅ Input results into notebook analysis section
7. ✅ Generate comparison charts

### STEP 3: Statistical Validation (2-3 hours)
1. ✅ Run statistical tests (already coded in notebook)
2. ✅ Check confidence intervals
3. ✅ Verify discriminatory gradient is smooth
4. ✅ Calculate effect sizes
5. ✅ Document any anomalies

### STEP 4: Writeup Revision (4-6 hours)
1. ✅ Update results section with new performance data
2. ✅ Add human baseline comparison
3. ✅ Include statistical significance findings
4. ✅ Add limitations section
5. ✅ Compare to existing benchmarks (literature review)
6. ✅ Polish abstract and conclusion

### STEP 5: Final Review (2-3 hours)
1. ✅ Proofread entire writeup
2. ✅ Check all citations
3. ✅ Verify code runs end-to-end
4. ✅ Test CSV export
5. ✅ Package all files for submission

---

## SUBMISSION CHECKLIST

### Required Files:
- [ ] Jupyter notebook (revised version)
- [ ] CSV results file (250 rows)
- [ ] Project writeup (PDF or Markdown)
- [ ] README with instructions
- [ ] (Optional) Human baseline data

### Required Sections in Writeup:
- [ ] Problem statement
- [ ] Task construction methodology
- [ ] Dataset description (250 cases, 5 paradigms)
- [ ] Evaluation framework (LLM judge)
- [ ] Results with statistics
- [ ] Human baseline comparison
- [ ] Insights and conclusions
- [ ] Limitations
- [ ] References

### Quality Checks:
- [ ] No redundant questions
- [ ] Balanced dataset (50 per paradigm)
- [ ] Smooth difficulty gradient
- [ ] Realistic cognitive tasks
- [ ] Proper SDK usage
- [ ] Clear documentation
- [ ] Statistical rigor
- [ ] Human validation

---

## TIMELINE TO SUBMISSION (26 days remaining)

### Week 1 (March 22-28): Foundation
- Day 1-2: Run revised notebook, validate output
- Day 3-4: Collect human baseline data
- Day 5-6: Analyze results, iterate on questions if needed
- Day 7: Rest and review

### Week 2 (March 29 - April 4): Analysis
- Day 8-9: Statistical analysis
- Day 10-11: Literature review for comparisons
- Day 12-13: Draft writeup revision
- Day 14: Rest and review

### Week 3 (April 5-11): Polish
- Day 15-16: Finalize writeup
- Day 17-18: Code cleanup and documentation
- Day 19-20: End-to-end testing
- Day 21: Rest and review

### Week 4 (April 12-16): Submission
- Day 22-23: Final proofreading
- Day 24: Package submission
- Day 25: Submit to Kaggle
- Day 26: Buffer for any issues

---

## SUCCESS METRICS

### Minimum Viable Submission:
- ✅ 250 unique, balanced questions
- ✅ Smooth difficulty gradient (not all 0% or 100%)
- ✅ LLM judge evaluation working
- ✅ Basic statistical analysis
- ✅ Complete writeup

### Competitive Submission:
- ✅ All of above PLUS:
- ✅ Human baseline with 10+ participants
- ✅ Confidence intervals and effect sizes
- ✅ Literature comparison
- ✅ Validated construct (actually measures IC)

### Prize-Winning Submission:
- ✅ All of above PLUS:
- ✅ Novel insights from results
- ✅ Comparison to multiple existing benchmarks
- ✅ Rigorous validation study
- ✅ Publication-ready quality

---

## RISK MITIGATION

### Risk 1: Performance still too low/high
**Mitigation:** Iterative calibration - run on small subset first, adjust difficulty

### Risk 2: Human baseline shows model outperforms humans
**Mitigation:** Good problem! Shows task is well-calibrated. Document this.

### Risk 3: No smooth gradient across tiers
**Mitigation:** Adjust tier definitions, add intermediate difficulty questions

### Risk 4: LLM judge is inconsistent
**Mitigation:** Run same question 3x, check variance. Adjust criteria if needed.

### Risk 5: Questions still have logical issues
**Mitigation:** Peer review - have 2-3 people review 10 random questions

---

## CONTACT FOR HELP

If you encounter issues:
1. Kaggle Discussion Forums (community help)
2. DeepMind contact (organizer questions)
3. Cognitive psychology forums (validation questions)
4. Statistics Stack Exchange (analysis help)

---

## FINAL ENCOURAGEMENT

You started with a 4/10 submission. With these fixes, you're targeting 8-9/10.

**The competition is winnable.** You have:
- ✅ A novel approach (Saliency Traps)
- ✅ Strong scientific framing
- ✅ Proper technical implementation
- ✅ 26 days to refine

**Next steps:**
1. Run the revised notebook (attached)
2. Collect human baseline this weekend
3. Analyze results next week
4. Submit with confidence by April 16

**You've got this!** 🚀🏆

---

## APPENDIX: Key Improvements Summary

| Aspect | Before | After | Impact |
|--------|--------|-------|--------|
| Dataset Size | 270 (90/90/30/30/30) | 250 (50/50/50/50/50) | Balanced |
| Unique Questions | ~27 | 250 | Real diversity |
| Evaluation | Regex + LLM (14%/25%) | LLM only (target 45-55%) | Scalable |
| Difficulty Gradient | Cliff drop (96%→0%) | Smooth (80%→50%→25%) | Discriminatory |
| False Binaries | 0% all tiers | 65%→40%→20% | Fixed |
| Human Baseline | None | Planned | Required |
| Statistics | None | Full analysis | Rigorous |
| Question Quality | Repetitive | Diverse | Professional |
