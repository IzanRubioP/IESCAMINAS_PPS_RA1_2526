// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MerkleStorage {
    address private owner;
    bytes32 public merkleRoot;

    event MerkleRootUpdated(bytes32 newRoot);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Solo el propietario puede ejecutar esta accion");
        _;
    }

    function setMerkleRoot(bytes32 _root) public onlyOwner {
        merkleRoot = _root;
        emit MerkleRootUpdated(_root);
    }

    function verify(bytes32 leaf, bytes32[] memory proof) public view returns (bool) {
        bytes32 computedHash = leaf;

        for (uint256 i = 0; i < proof.length; i++) {
            bytes32 proofElement = proof[i];

            if (computedHash < proofElement) {
                computedHash = keccak256(abi.encodePacked(computedHash, proofElement));
            } else {
                computedHash = keccak256(abi.encodePacked(proofElement, computedHash));
            }
        }

        return computedHash == merkleRoot;
    }
}
