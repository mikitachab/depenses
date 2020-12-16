import React from 'react';
import { ListGroup } from 'react-bootstrap';

function HistoryItemDebt(props) {
    return (
        <ListGroup>
            <ListGroup.Item className="history-item history-item-debt">
                <div>
                    <span className="history-item-price">{props.amount}</span>
                </div>
                <div>
                    <p className="history-item-buyer" style={{ textTransform: 'capitalize' }}>{props.description}</p>
                </div>
                <div>
                    <p className="history-item-owe">{props.fromMemberName} borrowed {props.toMemberName}</p>
                </div>
                <div>
                    <span className="history-item-date">{props.dateDetails}</span>
                </div>
            </ListGroup.Item>
        </ListGroup>
    )
}



export default HistoryItemDebt;