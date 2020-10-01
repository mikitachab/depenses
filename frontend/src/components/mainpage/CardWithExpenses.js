import React from 'react';

class CardWithExpenses extends React.Component {
    constructor() {
        super()
    }

    render() {
        return (
            <div className="card-item">
                <span>50$</span>
                <p>Irina</p>
            </div>
        )
    }

}



export default CardWithExpenses;
