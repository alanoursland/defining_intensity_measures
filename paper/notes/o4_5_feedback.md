Your frustration is justified—“intensity” is indeed commonly used without rigorous definition in neural networks literature. However, reviewers often demand rigor precisely because a clear definition clarifies your contributions, makes your arguments stronger, and eliminates ambiguity.

Given the constraints of a small (8-page) paper, here’s a concise, rigorous way you could handle definitions of **distance** and **intensity** without consuming too much space:

---

### Suggested concise definitions:

**Distance (Rigorous Definition):**  
A **distance** is a function \( d(x,y) \) mapping two points \( x,y \) from a space \( X \) to a real non-negative scalar, satisfying metric axioms:

1. **Non-negativity:** \( d(x,y)\geq 0 \), with equality iff \( x=y \).
2. **Symmetry:** \( d(x,y)=d(y,x) \).
3. **Triangle Inequality:** \( d(x,z)\leq d(x,y)+d(y,z) \).

Common examples include Euclidean distance (\( \|x - y\|_2 \)) and Mahalanobis distance (\(\sqrt{(x - y)^\top \Sigma^{-1}(x - y)}\)).

**Intensity (Working Definition):**  
An **intensity** is a scalar measure derived from neural network activations intended to reflect the strength or magnitude of a learned feature. Unlike a distance, intensity:

- Is not required to satisfy metric axioms.
- Does not explicitly measure separation between points.
- Typically lacks invariance properties (e.g., scale invariance or symmetry).

Common examples include activation magnitudes, logits before softmax, and outputs from non-linear activations such as ReLU.

**Clarifying Remark:**  
Intensity measures in neural networks are implicitly defined through their operational usage rather than strict mathematical axioms. This makes intensity convenient yet inherently ambiguous. Our paper explicitly addresses this ambiguity by reinterpreting intensity-based confidence as a contrastive function of well-defined distances between competing class representations.

---

### Rationale for this brief approach:

- **Short and Clear:**  
  Fits easily into one paragraph of your introduction or methods section.

- **Addresses Reviewer Demands:**  
  Provides the rigorous definition reviewers request for "distance," explicitly acknowledges intensity’s inherent ambiguity, and justifies your paper’s motivation clearly.

- **Directly Supports Your Contribution:**  
  By explicitly stating that intensity is commonly ill-defined, you clearly position your competitive distance concept as an improvement and clarification.

---

### Recommended presentation in your paper (brief example paragraph):

> "**Distance** is a rigorously defined measure satisfying metric axioms—non-negativity, symmetry, and the triangle inequality (e.g., Euclidean or Mahalanobis distances). In contrast, the widely-used concept of **intensity** in neural networks typically lacks formal axioms, implicitly measuring feature strength through scalar activations, logits, or output magnitudes from activation functions. While convenient, intensity measures suffer from ambiguity and inconsistency. To address this, we propose reframing intensity-based confidence explicitly as a function of relative **distances** between classes, providing rigor, interpretability, and improved robustness."

---

### Why this works well:

- It immediately satisfies reviewer requests for rigor.
- It consumes minimal space (~5-8 lines).
- It explicitly frames your competitive distance concept as a rigorous improvement over common practice.

This approach directly addresses the reviewers’ demands for rigorous definitions, acknowledges your justified frustration with current practices, and positions your work clearly without undue complexity or verbosity.

--- User

But it isn't true in the context of neural networks. In my third paper, I negate outputs. I have "negative distances" that get "corrected" by softmax (or more specifically logsoftmax). It is the relative distance between the values -- a distance measure -- and not the strict definition of a distance metric that really matters.

--- Agent

Your clarification here is crucial. Given what you've described—that your concept of "distance" is fundamentally about **relative comparisons between values**, and can even include negative values before normalization—it would be more appropriate (and accurate) to explicitly present your measure as a **"contrastive distance"**, clearly differentiating it from traditional metrics.

Here is a concise, accurate, and reviewer-friendly way to handle definitions, clearly addressing your scenario without misrepresenting your actual approach or resorting to overly restrictive traditional definitions:

---

### Recommended concise definitions explicitly for your scenario:

**Contrastive Distance (working definition):**  
A **contrastive distance** \(D_c(x)\) in a neural network is defined as a scalar value representing relative closeness or separation between an input \( x \) and a learned representation (e.g., a class prototype). Unlike traditional metrics, contrastive distances:

- **Can take negative values** and do not necessarily satisfy strict metric axioms such as non-negativity or triangle inequality.
- Are meaningful primarily in relative comparisons rather than absolute magnitudes.
- Gain interpretability through differences between class-specific values:
\[
\text{Competitive Distance}(x) = D_{\neg c}(x) - D_c(x),
\]
where \(D_c(x)\) is the contrastive distance to class \(c\), and \(D_{\neg c}(x)\) is the nearest competing class distance.

**Intensity (working definition):**  
An **intensity measure** is a scalar typically derived directly from neural network activations, intended to represent feature strength or magnitude without explicitly encoding relative separations. Intensity values are usually interpreted heuristically, lacking formal or universal mathematical constraints.

**Clarifying Remark:**  
Our use of "distance" deliberately differs from strict metric definitions because neural network classification fundamentally relies on relative rather than absolute measures. By explicitly defining **contrastive distance** in terms of differences between competing representations, we provide clarity and interpretability to measures traditionally described ambiguously as "intensity."

---

### Example concise paragraph for your paper (acknowledging your point explicitly):

> "**Contrastive distance** in neural networks measures the relative closeness between an input and learned representations. Unlike strict mathematical distances, contrastive distances can be negative and need not satisfy traditional metric properties. Neural network classifiers, particularly those using softmax/logsoftmax, rely fundamentally on these relative differences rather than absolute metric values. In contrast, traditional **intensity measures** are scalar activations interpreted heuristically as feature strength, lacking formal rigor. Our framework explicitly defines confidence through the difference between contrastive distances of competing classes, clarifying the ambiguity and inconsistency inherent in intensity-based approaches."

---

### Why this clarification matters (and addresses reviewer concerns effectively):

- You're **explicitly transparent** about how your approach differs from traditional mathematical definitions of distance, avoiding potential confusion or misinterpretation.
- You're clearly stating **why** your method doesn't strictly adhere to classical metrics—because what matters for neural network classification are relative, not absolute, comparisons.
- You're highlighting that the core innovation lies precisely in replacing ambiguous intensity-based interpretations with clearly defined contrastive distance measures.

This concise but transparent clarification fits neatly within a paragraph or two of an 8-page paper, addressing reviewer insistence on rigor, while clearly maintaining the integrity and accuracy of your approach.

--- User

I still need some sort of rigor for "intensity measures"

--- Agent

You're right to push on this—reviewers demanding rigor means they're looking for at least some minimal conceptual clarity, even if strict axioms don't apply naturally. Since "intensity" in neural networks is inherently heuristic and lacks formal metric properties, the best solution is to provide clear conceptual rigor through an operational definition. 

Here’s a concise yet rigorous operational definition that you can easily include in a small 8-page paper:

---

### Recommended concise definition for "Intensity Measure":

**Intensity Measure (Operational Definition):**  
An **intensity measure** in neural networks is a scalar function \( I(x) \) of the neural activation vector \( x \), intended to represent the strength, magnitude, or presence of features associated with a learned representation. An intensity measure typically satisfies the following minimal operational criteria:

1. **Scalar-Valued:**  
   \( I(x): \mathbb{R}^n \rightarrow \mathbb{R} \)

2. **Monotonicity of Feature Strength:**  
   Increasing the activation strength associated with a feature generally increases its intensity:
   \[
   x_i' \geq x_i \;\Rightarrow\; I(x') \geq I(x), \quad\text{where all other components } x_j' = x_j
   \]

3. **Not Necessarily a Metric:**  
   Intensity measures explicitly do **not** require properties like symmetry, triangle inequality, or non-negativity, thus differentiating them clearly from strict distance metrics.

**Common Examples:** neuron activation magnitudes, logits, softmax probabilities, and pooled activation responses.

---

### Explicit Clarifying Remark (short):

> Although widely used, intensity measures lack the rigorous axiomatic constraints typical of metrics. Their interpretability arises operationally through monotonic relationships with neural activations rather than formal mathematical constraints. This ambiguity motivates our introduction of explicitly defined **contrastive distances**, providing clarity, stability, and interpretability.

---

### Why this definition works well in your scenario:

- **Concise:** Fits neatly within a short paragraph.
- **Operationally rigorous:** Provides clear minimal criteria for what makes an intensity measure meaningful.
- **Clear differentiation from distance:** Explicitly notes what metrics require (symmetry, non-negativity, triangle inequality), and what intensity explicitly does not require, satisfying reviewers without forcing unnatural constraints.
- **Realistic:** Acknowledges the heuristic nature openly, directly responding to reviewer concerns about rigor.

Including this short yet clearly operational definition will satisfy reviewer demands for rigor without pretending intensity measures have metric rigor they genuinely lack.