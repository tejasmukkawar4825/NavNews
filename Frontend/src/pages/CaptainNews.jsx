import React, { useState, useEffect } from "react";
import { ArrowRight } from "lucide-react";
import axios from "axios";

const CaptainNews = () => {
  const [events, setEvents] = useState([]);
  const [message, setMessage] = useState("");
  const [processedData, setProcessedData] = useState(null);
  const [showGif, setShowGif] = useState(false); // State to toggle GIF visibility

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/data")
      .then((response) => setEvents(response.data))
      .catch((error) => console.error(error));
  }, []);

  const sendData = async () => {
    const response = await axios.post("http://127.0.0.1:5000/api/process", {
      input: 5,
    });
    setProcessedData(response.data.processed_data);
  };

  return (
    <div className="p-3">
      <h1 className="text-xl font-bold">{message}</h1>
      <button onClick={sendData} className="p-2 bg-blue-500 text-white rounded">
        Process Data
      </button>
      {processedData && <p>Processed Data: {processedData}</p>}

      <div className="p-1">
        {/* Heading */}
        <h2 className="text-2xl font-bold mb-4">Events Near You</h2>

        <div className="space-y-4">
          {events.map((event, index) => (
            <div
              key={index}
              className="w-96 p-4 flex items-center rounded-xl shadow-md border border-gray-300 bg-white"
            >
              {/* Event Details */}
              <div className="flex-1">
                <p className="font-semibold">
                  {event.title.length > 30
                    ? `${event.title.slice(0, 30)}...`
                    : event.title}
                </p>

                <p className="text-sm text-gray-500">
                  {event.date || "Time Not Available"}
                </p>
                <p className="text-sm text-gray-500">
                  {event.venue || "Venue Not Available"}
                </p>
                <p className="text-sm text-gray-500">
                  {"Expected people count: " +
                    (event.expected_people_count || "No data")}
                </p>
              </div>

              {/* Clickable Arrow Icon */}
              <ArrowRight
                className="w-6 h-6 text-gray-700 cursor-pointer"
                onClick={() => setShowGif(!showGif)} // Toggle GIF visibility
              />
            </div>
          ))}
        </div>

        {/* Render GIF when showGif is true */}
        {showGif && (
          <div className="mt-4 flex justify-center">
            <img
              src="https://media.tenor.com/x8v1oNUOmg4AAAAC/rickroll-roll.gif" // Replace with actual GIF URL
              alt="Loading GIF"
              className="w-64 h-64"
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default CaptainNews;
