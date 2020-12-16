import React from 'react';

function AddNewSettlement(props) {
    return (
        <form className="text-center" id="form" action="#!" onSubmit={props.onMakeSettlement}>
            <select defaultValue={'default'} className="form-control" onChange={props.onSelectSettlementUserChange}>
                <option value="default" disabled hidden>Choose Person</option>
                {
                    props.roomMembersWithoutMe.map((member, i) => (
                        <option key={i} value={member.id}>{member.name}</option>
                    ))}
            </select>
            <button className="add-btn btn btn-dark my-2">Add</button>
        </form >
    );
}



export default AddNewSettlement;
