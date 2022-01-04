from brownie import accounts, FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import deploy_mocks, get_account, Local_env


def deploy_fundme():
    account = get_account()
    if network.show_active() not in Local_env:
        price_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")


def main():
    deploy_fundme()
