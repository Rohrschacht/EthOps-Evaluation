#!/usr/bin/env python3

def main(filename: str):
    contract_addresses = []
    with open(filename) as f:
        for line in f:
            if "Contract address:" in line:
                fields = line.split()
                contract_addresses.append(fields[-1])

    with open('generated_DevOpsRegistry.bcql', 'w') as f:
        f.write('''
SET BLOCKCHAIN "Ethereum";

SET OUTPUT FOLDER "./test_output";
SET CONNECTION "ws://localhost:8545/";

string pid = "DevOpsRegistry";

BLOCKS (EARLIEST) (136) {
''')
        for address in contract_addresses:
            f.write('''
//    EMIT XES TRACE (pid)({0})({0} as xs:string concept:name);
    LOG ENTRIES ({0}) (NominateVoter(address nominee)) {{
//        EMIT XES EVENT (pid)({0})()("nominate voter" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("nominate voter" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (ReleaseVoter(address releasee)) {{
 //       EMIT XES EVENT (pid)({0})()("release voter" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("release voter" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (RoleBindingVoteCast(address voter, address subject, bool accepted)) {{
  //      EMIT XES EVENT (pid)({0})()("vote role-binding proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("vote role-binding proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (RoleBindingAccepted(address subject)) {{
   //     EMIT XES EVENT (pid)({0})()("accept role-binding" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("accept role-binding" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (RoleBindingRejected(address subject)) {{
    //    EMIT XES EVENT (pid)({0})()("reject role-binding" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("reject role-binding" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (VersionProposalCreated(bytes20 proposal)) {{
     //   EMIT XES EVENT (pid)({0})()("create version proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("create version proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (DeploymentProposalCreated(address proposal)) {{
    //    EMIT XES EVENT (pid)({0})()("create deployment proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("create deployment proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (VersionQuorumProposalCreated(uint newVersionQuorum)) {{
     //   EMIT XES EVENT (pid)({0})()("create version quorum proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("create version quorum proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (RoleBindingQuorumProposalCreated(uint newRoleBindingQuorum)) {{
     //   EMIT XES EVENT (pid)({0})()("create role-binding quorum proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("create role-binding quorum proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (VersionVoteCast(address voter, bytes20 proposal, bool accepted)) {{
     //   EMIT XES EVENT (pid)({0})()("vote version proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("vote version proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (DeploymentVoteCast(address voter, address proposal, bool accepted)) {{
     //   EMIT XES EVENT (pid)({0})()("vote deployment proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("vote deployment proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (QuorumVoteCast(address voter, bool accepted)) {{
     //   EMIT XES EVENT (pid)({0})()("vote quorum proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("vote quorum proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (VersionAccepted(bytes20 subject)) {{
     //   EMIT XES EVENT (pid)({0})()("accept version proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("accept version proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (VersionRejected(bytes20 subject)) {{
    //    EMIT XES EVENT (pid)({0})()("reject version proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("reject version proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (DeploymentAccepted(address subject)) {{
     //   EMIT XES EVENT (pid)({0})()("accept deployment proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("accept deployment proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (DeploymentRejected(address subject)) {{
    //    EMIT XES EVENT (pid)({0})()("reject deployment proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("reject deployment proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (QuorumAccepted()) {{
     //   EMIT XES EVENT (pid)({0})()("accept quorum proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("accept quorum proposal" as xs:string concept:name);
    }}
    LOG ENTRIES ({0}) (QuorumRejected()) {{
     //   EMIT XES EVENT (pid)({0})()("reject quorum proposal" as xs:string concept:name, block.timestamp as xs:date time:timestamp);
        EMIT XES EVENT (pid)({0})()("reject quorum proposal" as xs:string concept:name);
    }}
'''.format(address))
        f.write("}")

if __name__ == '__main__':
    main("node_output.txt")

