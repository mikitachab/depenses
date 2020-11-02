import React from 'react';
import { ListGroup } from 'react-bootstrap';

class HistoryItemExpense extends React.Component {
    render() {
        return (
            <ListGroup>
                <ListGroup.Item className="history-item history-item-expanse">
                    <div>
                        <span className="history-item-price">{this.props.price}</span>
                    </div>
                    <div>
                        <p className="history-item-buyer" style={{ textTransform: 'capitalize' }}>{this.props.description}</p>
                    </div>
                    <div>
                        <p className="history-item-buyer">{this.props.name}</p>
                    </div>
                    <div>
                        <span className="history-item-date">{this.props.dateDetails}</span>
                    </div>
                </ListGroup.Item>
            </ListGroup>
        )
    }

}



export default HistoryItemExpense;
