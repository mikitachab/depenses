import React from 'react';
import { Card } from 'react-bootstrap';
import DebtsDataOnCard from './DebtsDataOnCard'

function CardWithExpenses(props) {
    return (
        <Card className="card-item">
            <Card.Body>
                <Card.Title>{props.member.name}</Card.Title>
                {Object.keys(props.debt).map((memberName, i) => {
                    console.log(memberName)
                    return (
                        < DebtsDataOnCard name={memberName} amount={props.debt[memberName]} key={i} />
                    )
                })}
            </Card.Body>
        </Card >
    )
}



export default CardWithExpenses;