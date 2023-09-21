# STUN and TURN Server

WebRTC (Web Real-Time Communication) uses both `STUN` (Session Traversal Utilities for NAT) and `TURN` (Traversal Using Relays around NAT) servers to facilitate `peer-to-peer` communication in situations where direct communication between peers is hindered by network address translation (NAT) or firewall configurations.

Here's a brief description of STUN and TURN servers in WebRTC:

`STUN` (Session Traversal Utilities for NAT) Server:

- STUN servers are used to discover the public IP address and port of a device, which is essential for establishing a connection between two peers behind NAT or firewalls.
- They help in determining the network address translation (NAT) type, which aids in establishing direct peer-to-peer connections when possible.
- STUN servers don't relay media traffic; they only assist in the initial connection setup.
- STUN is used primarily for NAT traversal and works best when both peers can communicate directly after discovering their public addresses.

`TURN` (Traversal Using Relays around NAT) Server:

 - TURN servers act as intermediaries when direct peer-to-peer communication is not possible due to restrictive NAT or firewall configurations.
 - They relay media and data traffic between peers when direct connections fail, ensuring communication can occur.
 - TURN servers are typically used as a fallback when STUN alone cannot establish a direct connection.
 - While STUN is used to determine the public address of a device, TURN actively relays traffic between peers, making it a more versatile solution for addressing connectivity issues.

In WebRTC applications, developers can configure both STUN and TURN servers to handle various networking scenarios. These servers are crucial for achieving robust and reliable real-time communication over the internet, especially when dealing with the complexities of NAT traversal.