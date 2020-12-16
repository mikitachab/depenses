import React from 'react';
import { Card } from 'react-bootstrap';


function DebtsDataOnCard(props) {
    return (
        <Card.Text className="price">
            You owned {props.name} : {props.amount} $
        </Card.Text>
    )
}

export default DebtsDataOnCard;