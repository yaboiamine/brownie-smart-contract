this is my code walkthrough :
build folder where you can find the address of the deployed contract, to verify copy the address in the tail of the ".json" file and paste it in rinkeby block exploer.
contract folder where you find the contract source code (the ".sol" file).
scripts folder where there is python scripts to interact with the contract and the network where you are developing (be it local or a testnet network).
brownie-config.yaml file to override some default project configs (you can find more about it in brownie docs).
.env where you store your private key of your metamask wallet and infura project_id (i have put it in the .gitignore file because its a sensitive data).
