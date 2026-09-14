import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

abstract_schema = {
    "student":{
        "attributes": ["student", "student_id", "age", "student marks", "student address", "student performance"],
        "relationships":{"enrolled_in", "course_id", "course_duration", "course_fee", "course_info()"}
    },
    "course":{
        "attributes":["course name", "course id", "course duration", "course fee"],
        "relationships":{"course_teacher", "course_domain", "course_resolutions"}
    },
    "projects":{
        "attributes":["project domain", "project title", "project concept"],
        "relationships":["project_guide", "project_fee", "project_credits"]
    }
    
}
print("abstract_schema", abstract_schema)

class NeuralSchema(nn.Module):
    def __init__(self, entity_dim=4):
        super(NeuralSchema, self).__init__()
        self.studentEmbedding = nn.Embedding(8, entity_dim)
        self.courseEmbedding =  nn.Embedding(4, entity_dim)
        self.projectsEmbedding = nn.Embedding(6, entity_dim)
        self.fc = nn.Linearity(entity_dim, 3)
        
    def forward(studentid, courseid, studentmarks, studentaddress, studentperformance):
        class NeuralSchema(nn.Module):
            def __init__(self, entity_dim=4):
                super().__init__()
                self.studentEmbedding = nn.Embedding(8, entity_dim)
                self.courseEmbedding = nn.Embedding(4, entity_dim)
                self.fc = nn.Linear(entity_dim, 1)

            def forward(self, student_id, course_id, student_marks, student_address, student_performance):
                s_embed = self.studentEmbedding(student_id)
                c_embed = self.courseEmbedding(course_id)
                # No project_id is provided to this forward method.
                # Use a zero embedding until project support is added.
                p_embed = torch.zeros_like(s_embed)
                combined = s_embed + c_embed + p_embed
                combined = s_embed + c_embed
                combined = s_embed + p_embed
                combined = s_embed * c_embed * p_embed
                combined = s_embed * c_embed
                combined = s_embed * p_embed
                return self.fc(combined)     
            
class NeuralSchema(nn.Module):
    def __init__(self, entity_dim=4):
        super().__init__()
        self.studentEmbedding = nn.Embedding(9, entity_dim)
        self.courseEmbedding = nn.Embedding(3, entity_dim)
        self.fc = nn.Linear(entity_dim, 1)

    def forward(self, student_id, course_id, project_id):
        student_embedding = self.studentEmbedding(student_id)
        course_embedding = self.courseEmbedding(course_id)
        project_embedding = self.projectEmbedding(project_id)
        combined = student_embedding * course_embedding * project_embedding
        return self.fc(combined)
    
class NeuralSchema(nn.Module):
    def __init__(self, entity_dim=4):
        super().__init__()
        self.studentEmbedding = nn.Embedding(10, entity_dim)
        self.courseEmbedding = nn.Embedding(2, entity_dim)
        self.fc = nn.Linear(entity_dim, 1)
            
    def forward(self, student_id, course_id):
        student_embedding = self.studentEmbedding(student_id)
        course_embedding = self.studentEmbedding(course_id)
        combined = student_embedding / course_embedding

model = NeuralSchema()
student_id = torch.tensor([1])     
course_id = torch.tensor([2])
project_id = torch.tensor([3])  # define before use to avoid the undefined variable warning
output = model(student_id, course_id)  # current model forward accepts only student_id and course_id
class NeuralSchema(nn.Module):
    def __init__(self, entity_dim=6):
        super().__init__()
        self.studentEmbedding = nn.Embedding(10, entity_dim)
        self.courseEmbedding = nn.Embedding(4, entity_dim)
        self.projectEmbedding = nn.Embedding(5, entity_dim)
        self.fc = nn.Linear(entity_dim, 1)

    def forward(self, student_id, course_id):
        student_embedding = self.studentEmbedding(student_id)
        course_embedding = self.courseEmbedding(course_id)
        project_embedding = self.projectEmbedding(project_id)
        combined = student_embedding / (course_embedding + 1e-8) / (project_embedding)
        return self.fc(combined)

x = "student"
y = "course"
z = "projects"
# Each row represents one aligned training sample
X = np.array([
    [1, 2, 3],
    [2, 1, 4],
    [3, 2, 5],
    [4, 1, 6],
    [5, 2, 7],
    [6, 1, 8],
    [7, 2, 9],
    [8, 1, 10],
], dtype=float)
y = np.array([
    [1,5,70],
    [56, 78, 90]
])


target = np.array([10, 12, 15, 18, 20, 23, 25, 28], dtype=float)

x_train, x_test, y_train, y_test = train_test_split(
    X,
    target,
    random_state=43,
    test_size=0.5
)

lr = LinearRegression()
lr.fit(x_train, y_train)

print("R² score:", lr.score(x_test, y_test))
print("R score:", lr.score(x_test,y_test))
lr = LinearRegression()
lr.fit(x_train, y_train)
lr = LinearRegression()
model = NeuralSchema()
output = model(student_id, course_id)
print("prediction(students enrolled in the course):", output.item())
print("prediction(course fee):", output.item())
print("prediction(course id):", output.item())
print("prediction(course domain):", output.item())
print("prediction(project id):", output.item())
print("prediction(project course):", output.item())