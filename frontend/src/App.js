import React, { useState } from 'react';
import axios from 'axios';

const BookingForm = () => {
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [priority, setPriority] = useState(1);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/book_slot/', {
            start_time: startTime,
            end_time: endTime,
            priority: priority
        }).then(response => {
            alert('Booking successful');
        }).catch(error => {
            console.error("There was an error booking the slot!", error);
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="datetime-local" value={startTime} onChange={e => setStartTime(e.target.value)} required />
            <input type="datetime-local" value={endTime} onChange={e => setEndTime(e.target.value)} required />
            <input type="number" value={priority} onChange={e => setPriority(e.target.value)} required min="1" max="3" />
            <button type="submit">Book</button>
        </form>
    );
};

export default BookingForm;
