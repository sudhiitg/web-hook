import React, { useState, useEffect } from 'react';

export default function GetEvent() {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const res = await fetch('/api/events');
      const data = await res.json();
      setEvents(data);
    } catch (err) {
      console.error('Failed to fetch events:', err);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval); // Clean up interval on component unmount
  }, []);

  return (
    <ul>
      {events.map((event, index) => (
        <li key={index}>
          {event.type === 'push' && `${event.author} pushed to ${event.to_branch} on ${event.timestamp}`}
          {event.type === 'pull_request' && `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`}
          {event.type === 'merge' && `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`}
        </li>
      ))}
    </ul>
  );
};

