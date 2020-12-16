import React from 'react';
import CardWithExpenses from './CardWithExpenses';


function Cards(props) {
    return (
        <div className="card-expenses">
            {
                props.roomMembers.map((member, i) => {
                    return <CardWithExpenses
                        key={i}
                        member={member}
                        debt={props.roomState[member.name]}
                    />
                })
            }
        </div>
    );
}



export default Cards;