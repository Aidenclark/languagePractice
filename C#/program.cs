using System;
using System.Collections.Immutable;

class BankSystem {
    private ImmutableDictionary<int, decimal> accountBalances;

    public BankSystem() {
        accountBalances = ImmutableDictionary<int, decimal>.Empty;
    }

    public void AddOrUpdateAccount(int accountId, decimal balance) {
        accountBalances = accountBalances.SetItem(accountId, balance);
    }

    public decimal GetAccountBalance(int accountId) {
        return accountBalances.TryGetValue(accountId, out decimal balance) ? balance : 0;
    }
}

class Program {
    static void Main() {
        BankSystem bank = new BankSystem();
        bank.AddOrUpdateAccount(123, 1000.50m); // Adding an account with balance
        Console.WriteLine($"Account 123 Balance: {bank.GetAccountBalance(123)}");

        // Concurrently updating the account in a real application would be safe
        bank.AddOrUpdateAccount(123, 1100.75m); // Updating the same account
        Console.WriteLine($"Account 123 Updated Balance: {bank.GetAccountBalance(123)}");
    }
}
