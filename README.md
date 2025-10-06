# NavNews 🚗📱

A comprehensive ride-sharing application with real-time tracking, news updates, and seamless user experience for both passengers and drivers.

## 🌟 Features

### For Passengers
- **Real-time Ride Booking**: Book rides with live driver tracking
- **Location Search**: Find and select pickup and drop-off locations
- **Live Tracking**: Monitor your ride in real-time with GPS tracking
- **Driver Details**: View driver information and vehicle details
- **Ride History**: Track your past rides and payments
- **News Updates**: Stay informed with latest news while riding

### For Drivers (Captains)
- **Ride Management**: Accept, manage, and complete rides
- **Navigation**: Built-in maps and navigation support
- **Earnings Tracking**: Monitor your earnings and ride statistics
- **Profile Management**: Update personal and vehicle information
- **News Dashboard**: Access news updates and announcements

## 🏗️ Architecture

### Frontend
- **React.js**: Modern UI with component-based architecture
- **Tailwind CSS**: Responsive and beautiful styling
- **Socket.io**: Real-time communication
- **Vite**: Fast development and build tool

### Backend
- **Node.js**: Server-side JavaScript runtime
- **Express.js**: Web application framework
- **MongoDB**: NoSQL database for data persistence
- **Socket.io**: Real-time bidirectional communication
- **JWT**: Secure authentication and authorization

## 📁 Project Structure

```
Uber App News/
├── Frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── context/        # React context providers
│   │   └── hooks/          # Custom React hooks
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
├── Backend/                # Node.js backend application
│   ├── controllers/        # Request handlers
│   ├── models/            # Database models
│   ├── routes/            # API routes
│   ├── services/          # Business logic
│   ├── middlewares/       # Custom middleware
│   ├── db/               # Database configuration
│   └── package.json      # Backend dependencies
└── README.md             # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Node.js (v16 or higher)
- MongoDB
- Git

### Backend Setup

1. **Navigate to Backend directory**
   ```bash
   cd Backend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment variables**
   Create a `.env` file in the Backend directory:
   ```env
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret_key
   PORT=5000
   ```

4. **Start the server**
   ```bash
   npm start
   ```

### Frontend Setup

1. **Navigate to Frontend directory**
   ```bash
   cd Frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:5173`

## 🔧 API Endpoints

### Authentication
- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Rides
- `POST /api/rides/book` - Book a new ride
- `GET /api/rides/history` - Get ride history
- `PUT /api/rides/:id/status` - Update ride status

### Captains
- `POST /api/captains/signup` - Captain registration
- `POST /api/captains/login` - Captain login
- `GET /api/captains/available` - Get available captains

### Maps
- `GET /api/maps/geocode` - Geocoding service
- `GET /api/maps/directions` - Get directions

## 🎯 Key Features Implementation

### Real-time Tracking
- Socket.io integration for live location updates
- GPS coordinate tracking
- Real-time ride status updates

### Authentication System
- JWT-based authentication
- Role-based access control (User/Captain)
- Secure password hashing

### Database Models
- User Model: Passenger information
- Captain Model: Driver information
- Ride Model: Ride details and status
- BlackListToken Model: Token management

## 🛠️ Technologies Used

### Frontend
- React.js
- Tailwind CSS
- Socket.io Client
- Vite
- React Router

### Backend
- Node.js
- Express.js
- MongoDB
- Mongoose
- Socket.io
- JWT
- bcrypt

## 📱 Screenshots

*Add screenshots of your application here*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sujal1804**
- GitHub: [@Sujal1804](https://github.com/Sujal1804)

## 🙏 Acknowledgments

- React.js team for the amazing framework
- Tailwind CSS for the beautiful styling
- Socket.io for real-time communication
- MongoDB for the database solution

## 📞 Support

If you have any questions or need support, please open an issue on GitHub or contact the development team.

---

**Made with ❤️ by Sujal1804** 
