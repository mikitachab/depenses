import React from 'react';


function Room(props) {
    console.log(props.room);
    return (
        <div className="room-item">
            <p>{props.roomDetails.name}</p>
            <button className="btn btn-outline-warning">Choose that room</button>
        </div>
    );
}



export default Room;