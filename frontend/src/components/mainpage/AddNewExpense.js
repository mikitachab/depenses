import React from 'react';


function AddNewExpanse(props) {
    return (
        <form className="text-center" id="form" action="#!" onSubmit={props.onMakeExpense}>
            <input className="form-control" onChange={props.onInputDescriptionExpanseChange} type="text" placeholder="Add description" />
            <input className="form-control" onChange={props.onInputExpanseChange} type="number" placeholder="Enter amount of spending..." />
            <button className="add-btn btn btn-dark my-2">Add</button>
        </form>
    );
}



export default AddNewExpanse;