
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56"
    """
    num_positions = len(self.positions)
    cash_str = f"{self.cash:,.2f}"
    return f"{self.name} has {num_positions} positions and ${cash_str}"

