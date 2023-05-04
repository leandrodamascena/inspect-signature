from builder_example.builder.builder import Builder
from app_types import PersonalData, Education, FullData
import boto3

builder = Builder()

#Decorate this function to include signature to the build file
@builder.builder
def create_person(personal_data: PersonalData, education: Education) -> FullData:

    full_data = FullData(
        name=personal_data.name,
        age=personal_data.age,
        school=education.school,
        grade=education.grade,
    )
    return full_data


#Decorate this function to include signature to the build file
@builder.builder
def build_ec2_list(name: str, boto_client: boto3.Session) -> str:
    return name


person: FullData = create_person(PersonalData("leo", 39), Education("school one", 10.3))

ec2_client = boto3.client("ec2")
ec2_list: str = build_ec2_list("ec2_list", ec2_client)

#Flush to disk
builder.flush()
