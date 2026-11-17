from dataclasses import dataclass, field
from typing import List 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, confusion_matrix


@dataclass
class SelfEvidence:
    description : str
    support_schema : bool
    weight : float
    

@dataclass
class Selfschema:
    domain: str
    trait: str
    belief_strength: float
    evidence: List[SelfEvidence] = field(default_factory=list)
    learning_rate: float = 0.1

    def add_evidence(self, evidence: SelfEvidence):
        """Update the SelfSchema using new experiences and actions."""
        self.evidence.append(evidence)

        if evidence.support_schema:
            self.belief_strength += self.learning_rate * evidence.weight
        else:
            self.belief_strength += self.learning_rate * evidence.weight * 0.6

        self.belief_strength = max(0.0, min(1.0, self.belief_strength))

    def predict_success(self, task_difficulty: float):
        """Estimate likelihood of success in a related task."""
        return max(0.0, min(1.0, self.belief_strength - task_difficulty * 0.4))

    def choose_action(self, task_difficulty: float):
        """Use the SelfSchema to guide behavior."""
        success_probability = self.predict_success(task_difficulty)

        if success_probability >= 0.4:
            return "Attempt the Task Confidently"
        elif success_probability <= 0.3:
            return "Attempt With Preparation and Support"
        else:
            return "Practice first for Seeking of help"

    def summary(self):
        return {
            "domain": self.domain,
            "trait": self.trait,
            "belief_strength": round(self.belief_strength, 2),
            "evidence_count": len(self.evidence),
        }


learner_schema = Selfschema(
    domain="Academic performer",
    trait="Capable-Learner",
    belief_strength=0.60,
)

learner_schema.add_evidence(
    SelfEvidence(
        description="Completed a difficult numerical functions task",
        support_schema=True,
        weight=0.9,
    )
)

learner_schema.add_evidence(
    SelfEvidence(
        description="Failed one practice test",
        support_schema=False,
        weight=0.6,
    )
)

learner_schema.add_evidence(
    SelfEvidence(
        description="Passed one practice test",
        support_schema=True,
        weight=0.7
    )
)
    
print(learner_schema.summary())
print("Success prediction for medium task:", learner_schema.predict_success(0.5))
print("Recommended action:", learner_schema.choose_action(0.5))         
x = Selfschema
y = SelfEvidence
# x and y must be 2D feature data and 1D labels, not class objects
x = [
    [learner_schema.belief_strength, 1.0],
    [0.75, 1.0],
    [0.65, 0.0],
    [0.50, 0.0],
    [0.80, 1.0],
]
y = ["confident", "confident", "needs_support", "needs_support", "confident"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=43, test_size=0.4, stratify=y
)
model.fit(x_train, y_train)
model = KNeighborsClassifier()
model.fit(x_train, y_train)

# The training set has only 3 samples, so n_neighbors cannot exceed 3.
model.set_params(n_neighbors=min(3, len(x_train)))
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=0))
print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=0))
print("F1-score:", f1_score(y_test, y_pred, average='weighted', zero_division=0))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
x_pred = model.predict(x_test)
print("Prediction (y_pred):", y_pred)
print("accuracy_score(x_pred):", x_pred)
print("train_predictions(y_pred, x_pred):", y_pred, x_pred)
    
         