# ALP-ttbar Toy MC v1.5 — Preregistration: Two-Hypothesis Vertex Fit (Conversion vs. ALP Opening Angle) for Displaced Light ALP → e⁺e⁻

**Author:** Won Shik Paik (Independent Researcher, Auckland, New Zealand)
**Date frozen:** 2026-11-03 (this file is committed to GitHub before any v1.5 result for ALP pairs or photon conversions is computed)
**Builds on:** v1.4, https://doi.org/10.5281/zenodo.23880375 (toy study motivated by arXiv:2610.38932)
**Zenodo (this preregistration, PDF):** https://doi.org/10.5281/zenodo.23905511
**GitHub:** https://github.com/wspaik5/ALP_ttbar_Toy_MC_v1.5_Preregistration_Two_Hypothesis_Vertex_Fit
**Status:** plan only. No v1.5 outcome exists at the time of this commit.
**PDF version:** same text plus two figures drawn only from the formula in Sec. 0 and the published v1.3/v1.4
numbers (no new simulation).

---

## 0. Why v1.5

v1.4 found that a brems-aware fit (b) gives well-calibrated conversion vertices (pull width 0.95), but the limit
degradation from conversions stays large (17/50/100/200 MeV: 126×/68×/32×/14×, cτ = 1 mm). One reason is on the
signal side. Every pair, including ALP pairs, is fitted under the conversion hypothesis (tracks parallel at the vertex),
so the ALP opening angle is absorbed by a shift of the fitted vertex.

In the transverse plane, two tracks of opposite charge leaving a common point with opening Δφ separate as
Δφ·s + ½Δω·s² (Δω = |ω₁| + |ω₂|, ω = 1.14×10⁻³/pT[GeV] per mm at 3.8 T). A conversion-hypothesis fit can reproduce
this by moving the vertex by s₀ = Δφ/Δω along the track, leaving only a constant mismatch of Δφ²/(2Δω).
For pT = 10 GeV per leg (Δω ≈ 2.3×10⁻⁴ mm⁻¹):

| Δφ | vertex shift s₀ | remaining mismatch |
|---|---|---|
| 1 mrad (≈ 17 MeV) | ≈ 4 mm | ≈ 2 µm (below the 15 µm hit resolution) |
| 10 mrad (≈ 200 MeV) | ≈ 44 mm | ≈ 0.2 mm (clearly visible) |

v1.5 therefore fits each pair under **both** hypotheses. The χ² difference is used to exempt pairs with a visible opening
angle from the conversion veto. v1.5 also reports the combination of the v1.4 fits (a) and (b) as a secondary result.
A full Gaussian-sum filter (ACTS, C++) remains for a later version.

## 1. Questions

- **Q1 (primary).** With a two-hypothesis selection, how large is the limit degradation from conversions at 17, 50,
  100 and 200 MeV (cτ = 1 mm), compared with v1.4 fit (b) (126×, 68×, 32×, 14×) and the no-brems bound
  (1.9×, 2.0×, 1.9×, 1.8×)?
- **Q2.** How are the χ² differences distributed for conversions (bremsstrahlung tails can fake an opening angle) and
  for ALP pairs at each mass?

## 2. Unchanged from v1.4 (frozen)

- Mini simulation (`minitrack.py`): geometry, material, Highland scattering, Bethe–Heitler bremsstrahlung, hits.
- **Identical simulated hits:** the same samples, seeds and simulation calls as v1.3/v1.4 (conversions seed 5 /
  simulation seed 31; signal seed 11 / simulation seed 41), so v1.4 and v1.5 differ **only in the fit and selection**.
- **Conversion-hypothesis fit = v1.4 fit (b)** (brems-noise covariance and mean-loss track model, parallel-at-vertex
  constraint, 5 parameters, same starting points and tie-breaks). It is re-run only to keep χ² and fitted parameters,
  which v1.4 did not save. It must reproduce the v1.4 (b) vertex radii (Sec. 5).
- Pair-mass smearing (`bkg.measure`), base cuts, counting rule, metrics as in v1.1–v1.4.

## 3. The fits (frozen)

**H_conv (conversion hypothesis).** v1.4 fit (b), as above. Gives χ²_conv, the vertex radius r_conv and σ_conv.

**H_ALP (ALP hypothesis).** The same likelihood (same hits, covariance and track model as fit (b)), but the two track
directions at the vertex are free (6 parameters: x, y, φ₁, ω₁, φ₂, ω₂). It is **seeded from the H_conv solution**
(φ₂ = φ₁ at the start), so the nested model starts at the H_conv minimum and Gauss–Newton can only move downhill.
Gives χ²_ALP.

**Test statistic.** Δχ² = χ²_conv − χ²_ALP (one constraint). Without bremsstrahlung, conversions should follow χ²
with 1 degree of freedom. Only the transverse-plane opening angle is visible to this fit.

**(a)+(b) combination (secondary, single hypothesis).** Fit (b) using only the first N = 6 measured hits of each track
(v1.4 fit (a) selection), conversion hypothesis, v1.4 selection. Reported for completeness. It is not used in the
primary result.

## 4. Selection (frozen)

`scan_v15` extends `scan_v11`:
- **Exemption threshold** k ∈ {none, 1, 2, 4, 9, 16, 25, 49}. A pair with Δχ² ≥ k is "opening-angle-like" and is
  **exempt** from the material veto. All other pairs get the v1.1 material veto with (r_conv, σ_conv), band widened by
  nsig·σ_conv, nsig ∈ {none, 0.5, 1, 1.5, 2, 3, 4, 5}.
- The mass window is scanned as in v1.1. The best (k, nsig, mass window) is chosen per mass point on the same samples.
- k = none reproduces v1.4 (b) exactly. Because the v1.4 option is always included, the v1.5 degradation **cannot be
  larger** than v1.4 (b) by construction. The predictions below are therefore about the size of the gain.
- **Variant V-nomass.** In this toy, the pair mass (smeared directions) and Δχ² (hits) are generated independently.
  In a real detector both measure the same opening angle, so using both may overstate the separation. V-nomass disables
  the mass window in **both** v1.4 (b) and v1.5 and is reported next to the primary result.

## 5. Sanity gate (frozen)

Before any degradation is computed, for every sample:
1. **Identity.** H_conv reproduces the v1.4 (b) vertex radius within 10⁻⁶ mm for ≥ 99.9% of pairs.
2. **H_ALP fit.** Fit success ≥ 95%.
3. **Minimiser.** Fraction of pairs with Δχ² < −0.1 (H_ALP worse than its own starting point) ≤ 1%.

If the gate fails, the code is fixed, the failure and fix are reported, and the gate is re-run.

## 6. Validation (only samples independent of the outcome; criteria frozen)

- **X1 (null distribution, no brems).** The v1.3 V4 collinear pion-like sample (zero opening, seed 404), both
  hypotheses with fit (b) and c_k = 0. Median Δχ² between **0.30 and 0.65** (χ²₁ median 0.455). Fraction with
  Δχ² > 3.84 between **3% and 8%**.
- **X2 (response, no brems).** A new sample with a known opening angle (seed 606). Two tracks of opposite charge with
  pT = 10 GeV each, common vertex at r uniform in 30–300 mm, |η| < 1.0, Δφ ∈ {0, 2, 5, 10} mrad, brems off.
  The median Δχ² must **increase monotonically** with Δφ. The values are reported.

If a criterion fails, the code is fixed and the fix is reported.

## 7. Predictions (written before running)

- **P1 (17 MeV, primary).** Degradation **≥ 100×** (v1.4 (b): 126×). The opening is absorbed by a vertex shift of
  a few mm, so the gain is below 20%.
- **P2 (100 MeV, primary).** Degradation between **5× and 20×** (v1.4 (b): 32×).
- **P3 (200 MeV).** Degradation between **2× and 7×** (v1.4 (b): 14×).
- **P4 (50 MeV).** Degradation **≥ 34×**, i.e. a gain smaller than a factor of 2 (v1.4 (b): 68×).
- **P5 (mechanism).** Fraction of pairs with Δχ² > 9:
  - conversions (r < 800 mm): **5% to 25%** (bremsstrahlung tails fake an opening angle);
  - ALP 17 MeV: **≤ 20%**;
  - ALP 200 MeV: **≥ 60%**.
- **P6 ((a)+(b), secondary).** 17 MeV degradation within **±20%** of v1.4 (b), i.e. 101×–151×.

Each prediction is reported as confirmed or refuted against these ranges. Refuted predictions are not re-framed.

## 8. Reporting

v1.5 note with a Figure 8:
- (a) Δχ² distributions for conversions and the four ALP masses, with the χ²₁ curve;
- (b) degradation versus mass for v1.3 mode B, v1.4 (b), v1.5 two-hypothesis, (a)+(b), and the no-brems bound;
- (c) the V-nomass comparison.

The note also contains the X1/X2 validation, the prediction table, "Deviations from preregistration", "Limitations" and
"Future directions" (ACTS Gaussian-sum filter).

## 9. Limitations known in advance

- All v1.3–v1.4 limitations apply: transverse plane only, barrel only, idealised layers, no pattern recognition, toy
  material map, crude counting rule, selection optimised on the same samples.
- Fit (b) is a single-Gaussian approximation of the Bethe–Heitler loss. Large single energy losses can therefore
  produce large Δχ² for conversions.
- Truth is used for the material list, cosh η and the scattering momentum, as in v1.3/v1.4.
- Mass and Δχ² are treated as independent measurements (see V-nomass).
- The exempted pairs are not re-checked against material with the H_ALP vertex.
- Only trends and ratios are meaningful.

## 10. Outlook (context only, not tested in v1.5)

The mismatch Δφ²/(2Δω) in Sec. 0 scales as 1/B, because Δω is proportional to B. Both the conversion rate and
bremsstrahlung scale with the material budget. In this toy model, a lower field or less material should therefore make
a small opening angle easier to tell from a conversion, at the cost of momentum resolution. This is a trade-off, not a
case against high fields.

For context only (none of this is tested here):
- ALICE has recorded pp data at 13 TeV with the solenoid field reduced from 0.5 T to 0.2 T to extend dielectron
  measurements to low-pT electrons [A1].
- The FCC-ee detector concepts use about 2 T, a limit set by machine–detector-interface constraints [A2, A3].
- The ALICE 3 concept is built around a very low-material silicon tracker [A4].

A later version may repeat the mini simulation at a lower field and with reduced material to quantify this trade-off
in the toy model. No statement about the design or performance of real detectors is made.

[A1] ALICE Collaboration, Soft-dielectron excess in proton-proton collisions at √s = 13 TeV, arXiv:2005.14522.
[A2] N. Bacchetta et al., CLD – A Detector Concept for the FCC-ee, arXiv:1911.12230.
[A3] The IDEA detector concept for FCC-ee, arXiv:2502.21223.
[A4] ALICE Collaboration, Letter of intent for ALICE 3, arXiv:2211.02491.
