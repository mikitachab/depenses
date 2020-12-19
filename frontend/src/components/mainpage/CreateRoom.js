import React from 'react';


class CreateRoom extends React.Component {

    constructor() {
        super();
        this.state = {

        }
        this.roomNameRef = React.createRef();
    }





    render() {
        return (
            <div className="create-room container" >
                <form onSubmit={this.props.onHandleSubmit}>
                    <p className="my-2">Please create your room and name it</p>
                    <input ref={this.roomNameRef} type="text" className="form-control my-2" placeholder="Create room name" />
                    <input type="text" className="form-control my-2" placeholder="Add your group's member name " />
                    <button type="submit" className="btn btn-dark my-2">Create room</button>
                </form>
            </div>
        )
    }
}

export default CreateRoom;