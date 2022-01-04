from brownie import network, config, accounts, MockV3Aggregator
from brownie.network.main import show_active
from web3 import Web3

Forked_local_env = ["mainnet-fork-dev"]

Local_env = ["development", "ganache-local"]

decimals = 8
start_price = 200000000000


def get_account():
    if network.show_active() in Local_env or network.show_active() in Forked_local_env:
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"acitve network is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            decimals, Web3.toWei(start_price, "ether"), {"from": get_account()}
        )
