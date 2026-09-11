from federation.node import FederationNode
from federation.knowledge_exchange import KnowledgeExchange

germany = FederationNode(
    "node-1",
    "Germany"
)

japan = FederationNode(
    "node-2",
    "Japan"
)

germany.publish_knowledge(
    {
        "strategy": "left_wall",
        "reward": 0.9
    }
)

exchange = KnowledgeExchange()

exchange.transfer(
    germany,
    japan
)

print()

print("Germany:")
print(
    germany.get_knowledge()
)

print()

print("Japan:")
print(
    japan.get_knowledge()
)