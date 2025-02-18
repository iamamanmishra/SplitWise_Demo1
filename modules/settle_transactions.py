from modules.room_Transaction_Views import show_transactions_under_room
from utils.logger_config import logger


def settle_room_transactions(room_id, Authorization):
    try:
        # Get all the transactions for that particular room
        transactions = show_transactions_under_room(room_id, Authorization)

        # Initialize dictionary to track net amount owed by each user
        net_amount_owed = {}

        # Iterate over each transaction
        for transaction in transactions:
            # Calculate the number of members involved in fair split
            num_members = len(transaction['fairsplit_members'])

            # Calculate equal share amount
            equal_share_amount = transaction['amount'] / num_members

            # Update net amount owed by paid user (negative of total amount)
            net_amount_owed[transaction['paid_user_id']] = net_amount_owed.get(transaction['paid_user_id'], 0) - \
                                                           transaction['amount']

            # Update net amount owed to each member
            for member in transaction['fairsplit_members']:
                if member != transaction['paid_user_id']:
                    net_amount_owed[member] = net_amount_owed.get(member, 0) + equal_share_amount

        # Generate payment transactions
        payment_transactions = []
        for payer, amount in net_amount_owed.items():
            if amount != 0:
                for payee, owed_amount in net_amount_owed.items():
                    if amount < 0 and owed_amount > 0:
                        payment_amount = min(abs(amount), owed_amount)
                        payment_transactions.append({'payer': payer, 'payee': payee, 'amount': payment_amount})
                        amount += payment_amount
                        net_amount_owed[payer] += payment_amount
                        net_amount_owed[payee] -= payment_amount

        summary_list = []
        # Print payment transactions and add to summary list
        for payment in payment_transactions:
            settlement_json = {
                "payer": payment['payer'],
                "payee": payment['payee'],
                "amount": payment['amount']
            }
            # statement = f"{payment['payer']} owes Rs {payment['amount']:.2f} to {payment['payee']}"
            # print(statement)
            summary_list.append(settlement_json)
        logger.info("settle_room_transactions function executed successfully...")
        return summary_list

    except Exception as e:
        logger.exception(f"An error occurred while settling room transactions: {e}")
        print(f"An error occurred while settling room transactions: {e}")
