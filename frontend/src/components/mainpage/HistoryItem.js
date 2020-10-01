import React from 'react';

class HistoryItem extends React.Component {
    constructor() {
        super();
    }


    render() {
        return (
            <div className="history-item">
                <span className="history-item-price">{this.props.price}</span>
                <p className="history-item-buyer">{this.props.name}</p>
                <span className="history-item-date">{this.props.dateDetails}</span>
            </div>
        )
    }

}



export default HistoryItem;
