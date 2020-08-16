from aws_cdk import core

from infrastructure.infrastructure_stack import InfrastructureStack


app = core.App()
InfrastructureStack(app, "infrastructure", env={'region': 'us-west-2'})

app.synth()
