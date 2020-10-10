import React from 'react';


class AddNewExpanse extends React.Component {

    render() {
        return (
            <div className="add-new-expense">
                <form className="text-center" action="#!" onSubmit={this.props.createHistoryEl}>
                    <input className="form-control" onChange={this.props.onInputChange} type="number" id="input-to-add-expenses" placeholder="Enter amount of spending..." />
                    <button className="add-btn btn btn-dark my-2">Add</button>
                </form>
            </div>
        );
    }
}



export default AddNewExpanse;
