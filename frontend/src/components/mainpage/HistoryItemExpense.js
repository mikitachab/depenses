import React from 'react';
import { ListGroup } from 'react-bootstrap';

function HistoryItemExpense(props) {
    return (
        <ListGroup>
            <ListGroup.Item className="history-item history-item-expanse">
                <div>
                    <span className="history-item-price">{props.price}</span>
                </div>
                <div>
                    <p className="history-item-buyer" style={{ textTransform: 'capitalize' }}>{props.description}</p>
                </div>
                <div>
                    <p className="history-item-buyer">{props.name}</p>
                </div>
                <div>
                    <span className="history-item-date">{props.dateDetails}</span>
                </div>
            </ListGroup.Item>
        </ListGroup>
    )
}



export default HistoryItemExpense;
