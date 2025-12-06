
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    sym = sym.upper()

    pos = _find_position(self, sym)
    if pos is None:
        print("Symbol not in portfolio.")
        return

    if shares <= 0:
        return

    owned = pos.get("shares", 0)
    if shares > owned:
        print("Not enough shares to sell.")
        return

    proceeds = shares * price
    self.cash += proceeds

    total_shares = owned
    total_cost = pos.get("cost", 0.0)

    fraction = shares / total_shares
    cost_reduction = total_cost * fraction

    pos["shares"] = total_shares - shares
    pos["cost"] = total_cost - cost_reduction

    if pos["shares"] == 0:
        self.positions.remove(pos)


    return
       
