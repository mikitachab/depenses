import React from 'react';
import HistoryItem from './components/mainpage/HistoryItem';

class History extends React.Component {

    render() {
        { console.log(this.props.expenseData) }
        return (
            <div className="history">
                {this.props.expenseData.map((el, i) => {
                    return <HistoryItem name={el.member}
                        key={i}
                        price={el.amount}
                        dateDetails={this.props.getDate(el.date)} />
                })}
            </div>
        );
    }
}



export default History;
