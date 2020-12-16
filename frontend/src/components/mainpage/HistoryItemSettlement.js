import React from 'react';
import { ListGroup } from 'react-bootstrap';

function HistoryItemSettlement(props) {
    return (
        <ListGroup>
            <ListGroup.Item className="history-item history-item-settlement">
                <div>
                    <span>0.00</span>
                </div>
                <div>
                    <span className="history-item-price">Settlement with {props.settlement}</span>
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



export default HistoryItemSettlement;