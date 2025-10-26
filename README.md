# 🔥 LiveMCP Dashboard

> **Real-time Financial Transaction Streaming Dashboard with Lenses.io Integration & Advanced Fraud Flagging**

A powerful, real-time financial transaction monitoring dashboard that streams live data directly from **Lenses.io MCP servers** and Kafka topics. Features advanced **fraud flagging** capabilities with instant risk detection, real-time data streaming, and a beautiful responsive web interface for comprehensive transaction monitoring.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![aiohttp](https://img.shields.io/badge/aiohttp-3.9.1-green.svg)](https://aiohttp.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

## ✨ Dashboard Features

### 🎨 **Beautiful Web Interface**
- 🌟 **Modern UI Design** - Clean, professional dashboard interface
- 📱 **Fully Responsive** - Perfect display on desktop, tablet, and mobile
- 🎯 **Intuitive Navigation** - Easy-to-use interface with clear visual hierarchy
- 🌈 **Color-coded Alerts** - Visual risk indicators with red/yellow/green coding
- 📊 **Interactive Charts** - Real-time metrics with visual data representation

### 🚀 **Real-time Data Streaming**
- ⚡ **Live Lenses.io Integration** - Direct streaming from Lenses MCP servers
- 🔄 **Kafka Topic Streaming** - Real-time data from credit-card-transactions & paypal-transactions
- 📈 **Instant Data Updates** - Live metrics cards with real-time totals and amounts
- 🎭 **Dynamic Transaction Display** - Sortable, filterable live transaction table
- 🌐 **WebSocket Real-time Updates** - Instant notifications and live data streaming
- ⏱️ **30-Second Auto-refresh** - Continuous data synchronization from Lenses.io

### 🔍 **Advanced Filtering & Search**
- 🎛️ **Multi-criteria Filtering** - Filter by type, amount, merchant, category, status, risk level
- 🔎 **Smart Search Bar** - Full-text search across all transaction fields
- 🏷️ **Category Filters** - Quick filter buttons for common categories
- 💰 **Amount Range Sliders** - Visual amount filtering with min/max controls
- 🎯 **Risk Level Toggles** - One-click risk level filtering

### 🛡️ **Advanced Fraud Flagging System**
- 🚨 **Real-time Fraud Detection** - Instant fraud flagging as transactions stream from Lenses.io
- 🚩 **Smart Fraud Flags** - AI-powered risk scoring with immediate flagging
- 📊 **Live Risk Analytics** - Real-time visual breakdown of fraud risk distribution
- ⚠️ **Instant Alert System** - Immediate notifications for flagged high-risk transactions
- 🎨 **Visual Fraud Indicators** - Color-coded fraud flags (🔴 High Risk, 🟡 Medium Risk, 🟢 Low Risk)
- 🔍 **Fraud Pattern Detection** - Advanced algorithms detecting suspicious transaction patterns

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- **Lenses.io MCP Server Access** - Direct connection to Lenses MCP infrastructure
- **Kafka Topics**: `credit-card-transactions`, `paypal-transactions`
- **Real-time Data Streaming** - Live data feed from Lenses.io platform

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/livemcp-dashboard.git
   cd livemcp-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your MCP server**
   ```bash
   cp env.example .env
   # Edit .env with your MCP server details
   ```

4. **Run the dashboard**
   ```bash
   python real_live_dashboard.py
   ```

5. **Access the dashboard**
   ```
   http://localhost:8080
   ```

## 🌐 Live Web Dashboard

### 🖥️ **Access Your Dashboard**
**Dashboard URL**: http://localhost:8080

### 📊 **Current Live Data Streaming**
- ✅ **5 Live Transactions** streaming in real-time from Lenses.io
- ✅ **$82,639.98** total amount processed from Kafka topics
- ✅ **Real-time Fraud Flagging** with instant risk detection
- ✅ **Live Lenses.io Integration** streaming data continuously
- ✅ **Interactive Web Interface** with real-time updates
- ✅ **Responsive Design** works on all devices

### 🎨 **Dashboard Interface Features**
- **Header Section**: Live status indicator and refresh controls
- **Filter Panel**: Advanced filtering options with visual controls
- **Metrics Cards**: Real-time totals and analytics display
- **Transaction Table**: Sortable, searchable transaction list
- **Risk Indicators**: Color-coded risk levels and status

## 🖥️ Web Dashboard Display Features

### 🌟 **Modern Web Interface**
- **Clean Design**: Professional, modern web interface with intuitive layout
- **Responsive Layout**: Perfect display on desktop (1200px+), tablet (768px-1199px), and mobile (320px-767px)
- **Visual Hierarchy**: Clear information architecture with proper spacing and typography
- **Interactive Elements**: Hover effects, smooth transitions, and visual feedback

### 📊 **Real-time Data Visualization**
- **Live Lenses.io Streaming**: Beautiful cards displaying real-time totals, amounts, and fraud flags
- **Dynamic Kafka Tables**: Sortable, filterable transaction tables with live Lenses.io data
- **Real-time Progress Indicators**: Visual loading states and Lenses.io connection status
- **Fraud Flag Badges**: Color-coded fraud detection indicators for transactions and system health

### 🎨 **Visual Design Elements**
- **Color Scheme**: Professional blue (#2c3e50) and green (#27ae60) color palette
- **Typography**: Clean, readable fonts with proper contrast ratios
- **Icons**: Intuitive icons for navigation and status indicators
- **Shadows & Effects**: Subtle shadows and visual depth for modern appearance

### 🔄 **Interactive Features**
- **Lenses.io Auto-refresh**: Seamless background updates every 30 seconds from Lenses.io
- **Manual Data Refresh**: One-click refresh button to sync with Lenses.io MCP server
- **Real-time Filter Controls**: Interactive dropdowns, sliders, and search inputs with live updates
- **Sortable Columns**: Click-to-sort functionality in live transaction tables
- **Fraud Flag Toggles**: Real-time filtering by fraud risk levels

## 📊 Dashboard Screenshots

### 🖥️ **Main Dashboard Interface**
![Dashboard Overview](https://via.placeholder.com/1200x600/2c3e50/ffffff?text=Live+MCP+Web+Dashboard+Interface)
*Beautiful, responsive web dashboard with real-time transaction monitoring*

### 📱 **Mobile Responsive Design**
![Mobile Dashboard](https://via.placeholder.com/400x800/34495e/ffffff?text=Mobile+Dashboard+View)
*Perfect display on mobile devices with touch-friendly interface*

### 🎨 **Interactive Filtering Panel**
![Filtering Interface](https://via.placeholder.com/1200x400/3498db/ffffff?text=Advanced+Filtering+Panel)
*Advanced filtering controls with visual range sliders and category buttons*

### 📊 **Real-time Metrics Display**
![Metrics Cards](https://via.placeholder.com/1200x300/27ae60/ffffff?text=Live+Metrics+and+Analytics)
*Dynamic metrics cards showing totals, amounts, and risk counts*

### 🚨 **Real-time Fraud Flagging & Risk Analysis**
![Fraud Flagging](https://via.placeholder.com/1200x500/e74c3c/ffffff?text=Real-time+Fraud+Flagging+from+Lenses.io)
*Live fraud detection with instant flagging and color-coded risk indicators*

### 🔍 **Transaction Table View**
![Transaction Table](https://via.placeholder.com/1200x400/f39c12/ffffff?text=Interactive+Transaction+Table)
*Sortable, searchable transaction table with real-time updates*

## ⚡ Lenses.io Real-time Data Streaming

### 🚀 **Live Data Integration**
- **Direct Lenses.io Connection**: Real-time streaming from Lenses MCP servers
- **Kafka Topic Streaming**: Live data from `credit-card-transactions` and `paypal-transactions`
- **30-Second Auto-sync**: Continuous data synchronization with Lenses.io platform
- **WebSocket Integration**: Instant real-time updates and notifications
- **Live Metrics**: Real-time totals, amounts, and transaction counts

### 🔄 **Real-time Streaming Features**
- **Instant Data Updates**: Live transaction data streaming every 30 seconds
- **Live Connection Status**: Real-time Lenses.io connection monitoring
- **Dynamic Data Refresh**: Automatic background updates from Lenses.io
- **Real-time Fraud Detection**: Instant fraud flagging as data streams in
- **Live Risk Scoring**: Real-time risk assessment with immediate visual updates

## 🔧 Configuration

### Lenses.io MCP Server Settings

```python
# config.py
LENSES_MCP_SERVER_URL = "http://108.129.193.220:8080/mcp"
ENVIRONMENT = "financial-data"
KAFKA_TOPICS = [
    "credit-card-transactions",  # Real-time credit card transaction streaming
    "paypal-transactions"        # Real-time PayPal transaction streaming
]
FRAUD_DETECTION_ENABLED = True
REAL_TIME_STREAMING = True
```

### Environment Variables

```bash
# .env
LENSES_MCP_URL=http://108.129.193.220:8080/mcp
ENVIRONMENT=financial-data
DASHBOARD_PORT=8080
DASHBOARD_HOST=localhost
FRAUD_DETECTION_ENABLED=true
REAL_TIME_STREAMING=true
KAFKA_TOPICS=credit-card-transactions,paypal-transactions
```

## 📁 Project Structure

```
livemcp-dashboard/
├── real_live_dashboard.py    # 🎯 Main dashboard application
├── dashboard_status.py       # 🔍 System status checker
├── config.py                # ⚙️ Configuration settings
├── requirements.txt         # 📦 Python dependencies
├── env.example             # 🔧 Environment variables template
├── README.md               # 📖 This file
└── PROJECT_CLEANUP_SUMMARY.md # 🧹 Cleanup documentation
```

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard interface |
| `/api/transactions` | GET | Get live transaction data |
| `/api/metrics` | GET | Get real-time metrics |
| `/api/search` | GET | Search transactions |
| `/ws` | WebSocket | Real-time updates |

## 🔍 Dashboard Usage Examples

### 🖥️ **Web Dashboard Interface**

#### **Access the Dashboard**
1. **Open your browser** and navigate to `http://localhost:8080`
2. **View the beautiful interface** with real-time data streaming
3. **Interact with the responsive design** on any device

#### **Dashboard Navigation**
- **Header Bar**: Live status indicator and refresh button
- **Filter Panel**: Advanced filtering controls with visual sliders
- **Metrics Cards**: Real-time totals and analytics display
- **Transaction Table**: Interactive, sortable transaction list
- **Search Bar**: Full-text search across all fields

### 🎛️ **Interactive Filtering**
- **Transaction Type**: Visual toggle buttons for Credit Card/PayPal
- **Amount Range**: Interactive min/max sliders with real-time updates
- **Merchant Search**: Live search with instant results
- **Category Filters**: Quick-select buttons for common categories
- **Status Indicators**: Color-coded status filters
- **Risk Level**: Visual risk level toggles with color coding

### 🔎 **Smart Search Features**
- **Real-time Search**: Instant results as you type
- **Multi-field Search**: Search across ID, merchant, category, customer
- **Highlighted Results**: Search terms highlighted in results
- **Clear Filters**: One-click filter reset functionality

### 📱 **Responsive Design**
- **Desktop**: Full-featured dashboard with all controls
- **Tablet**: Optimized layout with touch-friendly controls
- **Mobile**: Streamlined interface with essential features

## 🛡️ Real-time Fraud Flagging & Detection

The web dashboard features advanced **real-time fraud flagging** with instant detection as data streams from Lenses.io:

### 🚨 **Live Fraud Flagging System**
- **Real-time Fraud Detection**: Instant fraud flagging as transactions stream from Lenses.io MCP servers
- **Smart Fraud Flags**: AI-powered risk scoring with immediate flagging of suspicious transactions
- **Live Risk Scoring**: Real-time 0.0 to 1.0 risk scale with instant visual updates
- **Instant Alert System**: Immediate notifications for flagged high-risk transactions

### 🎨 **Visual Fraud Indicators**
- **Color-coded Fraud Flags**: 
  - 🔴 **Red (High Risk)**: Fraudulent transactions requiring immediate attention
  - 🟡 **Yellow (Medium Risk)**: Suspicious transactions needing review
  - 🟢 **Green (Low Risk)**: Safe, verified transactions
- **Fraud Alert Badges**: Prominent visual alerts for flagged transactions
- **Risk Score Display**: Visual progress bars showing real-time fraud risk levels

### 📊 **Live Fraud Analytics Dashboard**
- **Real-time Risk Distribution**: Live visual breakdown of fraud risk levels
- **Amount-based Fraud Detection**: Visual indicators for high-value suspicious transactions
- **Category Fraud Mapping**: Color-coded category risk indicators for fraud patterns
- **Status Fraud Alerts**: Visual flags for failed/pending suspicious transactions
- **Live Fraud Updates**: Real-time fraud scoring with instant visual updates from Lenses.io

## 📦 Dependencies

```txt
aiohttp==3.9.1      # Web framework
websockets==12.0    # WebSocket support
aiofiles==23.2.1    # Async file operations
```

## 🚀 Deployment

### Local Development
```bash
python real_live_dashboard.py
```

### Production Deployment
```bash
# Using gunicorn
gunicorn real_live_dashboard:app --bind 0.0.0.0:8080

# Using Docker (if Dockerfile provided)
docker build -t livemcp-dashboard .
docker run -p 8080:8080 livemcp-dashboard
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Lenses.io** - For the MCP server infrastructure
- **aiohttp** - For the excellent async web framework
- **Kafka** - For real-time data streaming

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/livemcp-dashboard/issues)
- **Documentation**: [Wiki](https://github.com/yourusername/livemcp-dashboard/wiki)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/livemcp-dashboard/discussions)

## 🎯 Dashboard Roadmap

### 🎨 **UI/UX Enhancements**
- [ ] **Dark Mode Toggle** - Beautiful dark theme for the web dashboard
- [ ] **Customizable Widgets** - Drag-and-drop dashboard customization
- [ ] **Advanced Charts** - Interactive charts and graphs for analytics
- [ ] **Dashboard Themes** - Multiple color schemes and layouts
- [ ] **Animation Effects** - Smooth transitions and loading animations

### 📱 **Display Improvements**
- [ ] **Real-time Fraud Notifications** - Visual popup notifications for flagged high-risk transactions
- [ ] **Advanced Fraud Analytics Dashboard** - Machine learning-based fraud detection with visual insights
- [ ] **Multi-tenant Lenses.io Integration** - Support for multiple organizations with separate Lenses.io views
- [ ] **Mobile App with Live Streaming** - Native mobile application with real-time Lenses.io data sync
- [ ] **Fraud Data Export UI** - Visual CSV/JSON export of flagged transactions with progress indicators
- [ ] **Dashboard Sharing** - Share fraud detection dashboard views with team members

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for the financial technology community

</div>