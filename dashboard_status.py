#!/usr/bin/env python3
"""
Dashboard Status Check
Shows the current status of the Financial Data Dashboard
"""

import requests
import json
from datetime import datetime

def check_dashboard_status():
    """Check if the dashboard is running and show status"""
    
    print("="*60)
    print("FINANCIAL DATA DASHBOARD - STATUS CHECK")
    print("="*60)
    print(f"Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Check if dashboard is running
        print("Checking dashboard status...")
        
        # Test metrics endpoint
        metrics_response = requests.get("http://localhost:8080/api/metrics", timeout=5)
        if metrics_response.status_code == 200:
            metrics_data = metrics_response.json()
            print("+ Dashboard is RUNNING")
            print("+ Metrics API is working")
            print()
            
            print("CURRENT METRICS:")
            print("-" * 30)
            print(f"Total Transactions: {metrics_data.get('total_transactions', 0)}")
            print(f"Total Amount: ${metrics_data.get('total_amount', 0):.2f}")
            print(f"High Risk Count: {metrics_data.get('high_risk_count', 0)}")
            print(f"Fraud Cases: {metrics_data.get('fraud_count', 0)}")
            print(f"Last Updated: {metrics_data.get('timestamp', 'Unknown')}")
            print()
            
            # Test transactions endpoint
            transactions_response = requests.get("http://localhost:8080/api/transactions", timeout=5)
            if transactions_response.status_code == 200:
                transactions_data = transactions_response.json()
                print("+ Transactions API is working")
                print(f"+ Loaded {len(transactions_data.get('transactions', []))} transactions")
                print()
                
                # Show sample transactions
                transactions = transactions_data.get('transactions', [])
                if transactions:
                    print("SAMPLE TRANSACTIONS:")
                    print("-" * 30)
                    for i, tx in enumerate(transactions[:3]):  # Show first 3
                        print(f"{i+1}. {tx.get('transaction_id', 'N/A')} - {tx.get('merchant', 'N/A')} - ${tx.get('amount', 0):.2f} - {tx.get('risk_level', 'N/A')}")
                    if len(transactions) > 3:
                        print(f"   ... and {len(transactions) - 3} more transactions")
                    print()
                
            else:
                print("- Transactions API error")
                
        else:
            print("- Dashboard is not responding")
            print(f"Status Code: {metrics_response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("- Dashboard is NOT RUNNING")
        print("   Start it with: python start_dashboard.py")
    except Exception as e:
        print(f"- Error checking dashboard: {e}")
    
    print("="*60)
    print("DASHBOARD ACCESS:")
    print("="*60)
    print("Web Interface: http://localhost:8080")
    print("API Endpoints:")
    print("  - Metrics: http://localhost:8080/api/metrics")
    print("  - Transactions: http://localhost:8080/api/transactions")
    print("  - Search: http://localhost:8080/api/search")
    print("  - WebSocket: ws://localhost:8080/ws")
    print()
    print("FEATURES AVAILABLE:")
    print("- Real-time transaction monitoring")
    print("- Advanced filtering and search")
    print("- Fraud detection and risk scoring")
    print("- Live metrics and analytics")
    print("- Auto-refresh every 30 seconds")
    print()
    print("To stop the dashboard: Press Ctrl+C in the terminal where it's running")

if __name__ == "__main__":
    check_dashboard_status()
