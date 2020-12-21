import React from 'react';
import { Card } from 'react-bootstrap';


function DebtsDataOnCard(props) {
    return (
        <Card.Text className="price text-center">
            You owned {props.name} : {props.amount} $
        </Card.Text>
    )
}

export default DebtsDataOnCard;