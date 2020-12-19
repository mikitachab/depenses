import React from 'react';
import History from './History';
import NavBarComponent from './NavBarComponent';
import AddNewExpanseOrDebt from './AddNewExpanseOrDebt';
import Cards from './Cards';
import Error from '../../Error';
import DepensesApi from '../../api';


import axios from 'axios';
class MainPage extends React.Component {
    constructor() {
        super();
        this.state = {
            expenseData: [],
            inputExpanse: '',
            inputDescriptionExpanse: '',
            inputDescriptionDebt: '',
            settlement: false,
            selectValue: 'expanses',
            error: false,
            actualUser: '',
            roomMembers: [],
            roomMembersWithoutMe: [],
            roomState: {},
            selectedDebtMemberId: {},
            selectedDebtMemberName: {},
            selectedSettlementMember: {},
            requiresCreateRoom: null,
            roomId: null,
            roomName: null,
            currency: '',
            arrayWithAllRooms: [],
            selectedRoom: {}

        }
        this.api = new DepensesApi();
        this.roomNameRef = React.createRef();
    }
    chooseRoom = (room) => {
        console.log(room.id);
        this.setState({
            selectedRoom: room,
            roomId: room.id,
            roomName: room.name,
            currency: room.currency
        });
        console.log(this.state.roomId);
    }

    getRoomMemberData = async () => {
        try {
            const response = await this.api.makeRoomMemberRequest('users/rooms/');
            if (response.data.length !== 0 && Object.keys(this.state.selectedRoom).length === 0) {
                console.log('take first el');
                this.setState({
                    requiresCreateRoom: true,
                    roomName: response.data[0].name,
                    currency: response.data[0].currency,
                    roomId: response.data[0].id
                })
            } else if (Object.keys(this.state.selectedRoom).length >= 1) {
                console.log('seco');
                this.setState({
                    roomId: this.state.selectedRoom.id,
                    roomName: this.state.selectedRoom.name,
                    currency: this.state.selectedRoom.currency
                });
            }


            console.log(this.state.roomId);


            this.setState({ arrayWithAllRooms: response.data });

            console.log(this.state.arrayWithAllRooms)
        } catch (error) {
            console.log(error);
        }
    }

    getToken() {
        return window.localStorage.getItem('x-auth-token')
    }

    onHandleChange = (e) => {

    }

    onInputExpanseChange = (e) => {
        let newExpansesEl = parseInt(e.target.value);
        this.setState({ inputExpanse: newExpansesEl });
    }

    onInputDescriptionExpanseChange = (e) => {
        let newExpansesEl = e.target.value;
        this.setState({ inputDescriptionExpanse: newExpansesEl });
    }

    onInputDescriptionDebtChange = (e) => {
        let newExpansesEl = e.target.value;
        this.setState({ inputDescriptionDebt: newExpansesEl });
    }

    onSelectChange = (e) => {
        let newSelectValue = e.target.value;
        this.setState({ selectValue: newSelectValue });
    }

    onSelectDebtUserChange = (e) => {
        let newSelectValue = e.target.value;
        this.setState({
            selectedDebtMemberId: newSelectValue.id,
            selectedDebtMemberName: newSelectValue.name
        });
    }


    getMemberNameById = (memberId) => {
        return this.state.roomMembers.filter(member => member.id === memberId)[0];
    }

    onSelectSettlementUserChange = (e) => {
        const selectedMemberId = parseInt(e.target.value);
        const selectedMember = this.getMemberNameById(selectedMemberId);

        this.setState({
            selectedSettlementMember: selectedMember,
        });
    }

    onMakeSettlement = async (e) => {
        e.preventDefault();

        const response = await this.api.makeApiPostRequest("settlements", {
            member: this.state.actualUser.id,
            member_name: this.state.selectedSettlementMember.name,
            settlement_with_member: this.state.selectedSettlementMember.id,
            settlement_with_member_name: this.state.selectedSettlementMember.name,
            room: this.state.roomId
        })
        console.log(response.data)

        this.setState({
            expenseData: [{
                member: this.state.actualUser.id,
                member_name: this.state.actualUser.name,
                settlement_with_member: this.state.selectedSettlementMember.name,
                settlement_with_member_name: this.state.selectedSettlementMember.name,
                settlement: true,
                date: new Date,
                type: 'settlement'
            }, ...this.state.expenseData]
        })

        this.updateResponseState()
    }
    onMakeDebt = async (e) => {
        e.preventDefault();
        const response = await this.api.makeApiPostRequest("depts", {
            title: this.state.inputDescriptionDebt,
            member: parseInt(this.state.actualUser.id),
            amount: this.state.inputExpanse,
            from_member: parseInt(this.state.actualUser.id),
            to_member: this.state.selectedDebtMember.id,
            room: this.state.roomId
        });


        this.setState({
            expenseData: [{
                member: this.state.actualUser.id,
                amount: this.state.inputExpanse,
                from_member_name: this.state.actualUser.name,
                to_member_name: this.state.selectedDebtMember.name,
                title: this.state.inputDescriptionDebt,
                date: new Date,
                type: 'dept'
            },
            ...this.state.expenseData
            ]
        })
        this.updateResponseState()
    }

    onMakeExpense = async (e) => {
        console.log(this.state.selectedRoom.id)
        const response = await this.api.makeApiPostRequest("spendings", {
            amount: this.state.inputExpanse,
            title: this.state.inputDescriptionExpanse,
            member: this.state.actualUser.id,
            room: this.state.roomId
        })
        console.log(response.data)

        this.setState({
            expenseData: [{
                amount: this.state.inputExpanse,
                title: this.state.inputDescriptionExpanse,
                member_name: this.state.actualUser.name,
                date: new Date,
                type: 'spending'
            }, ...this.state.expenseData]
        })
        this.updateResponseState()
    }

    uploadInfoAboutRoomMember = async () => {
        try {
            console.log(this.state.roomId);
            await this.getRoomMemberData();
            await this.updateResponseState();
            const getHistoryDataResponse = await this.api.makeRoomEndpointRequest('history', this.state.roomId);
            this.setState({
                expenseData: [...this.state.expenseData, ...getHistoryDataResponse.data]
            })
            console.log(getHistoryDataResponse)
            const getActualUserNameResponse = await this.api.makeRoomEndpointRequest('me', this.state.roomId);
            this.setState({
                actualUser: getActualUserNameResponse.data
            })
        }
        catch (err) {
            if (!err.response) {
                this.setState({ error: 'Unknown error' });
                console.log('Unknown error');
            } else if (err.response.status === 500) {
                this.setState({ error: 'Server error' })
                console.log('Server error');
            } else {
                this.setState({ error: 'Bad Request' })
                console.log('Bad Request');
            }
        }
    }

    componentDidMount = () => {
        this.uploadInfoAboutRoomMember();

        const roomMembersWithoutMe = this.state.roomMembers.filter((member) => {
            return member.name !== this.state.actualUser.name;
        })

        this.setState({
            roomMembersWithoutMe: roomMembersWithoutMe,
            selectedDebtMember: roomMembersWithoutMe[0]
        })
    }

    updateResponseState = async () => {
        const responseMembers = await this.api.makeRoomEndpointRequest('members', this.state.roomId);
        const responseState = await this.api.makeRoomEndpointRequest('state', this.state.roomId);
        this.setState({ roomMembers: responseMembers.data, roomState: responseState.data });
    }


    getDate = (date) => {
        var newDate = new Date(date);
        var day = newDate.getDate().toString();
        var month = newDate.getMonth().toString();
        var year = newDate.getFullYear().toString();

        return `${day.padStart(2, '0')}.${month.padStart(2, '0')}.${year.padStart(2, '0')}`;
    }




    onHandleSubmitRoomMember = async (e) => {
        e.preventDefault();
        try {
            const response = await this.api.makeRoomMemberPostRequest('users/rooms/', {
                "name": this.roomNameRef.current.value,
                "currency": 'EUR'
            })
            if (response.status === 200) {
                this.setState({ requiresCreateRoom: true })
            } else {
                this.setState({
                    requiresCreateRoom: false
                })
            }
        } catch (error) {
            console.log(error);
        }
    }


    render() {
        let createRoom = this.state.requiresCreateRoom;
        return (
            <div>
                <NavBarComponent />
                <div className="container-fluid mainpage" >
                    <div className="row-mainpage">
                        <div className="content-row container">
                            <div className="row">
                                <div className="choose-create-room">
                                    <p className="text-right">
                                        <button className="btn btn-dark" type="button" data-toggle="collapse" data-target=".multi-collapse" aria-expanded="false" aria-controls="multiCollapseExample1 multiCollapseExample2">Choose or Create Other Room</button>
                                    </p>
                                    <div className="row">
                                        <div className="col">
                                            <div className="collapse multi-collapse" id="multiCollapseExample1">
                                                <div className="card card-body">
                                                    <div className="create-room container" >
                                                        <form onSubmit={this.onHandleSubmitRoomMember}>
                                                            <p className="my-2">Please create your room and name it</p>
                                                            <input ref={this.roomNameRef} type="text" className="form-control my-2" placeholder="Create room name" />
                                                            <input type="text" className="form-control my-2" placeholder="Add your group's member name " />
                                                            <button type="submit" className="btn btn-dark my-2">Create room</button>
                                                        </form>
                                                    </div>
                                                    <div className="text-right room-details">
                                                        {this.state.arrayWithAllRooms.map((room, i) => {
                                                            return (
                                                                <div className="room-item" key={i}>
                                                                    <p>{room.name}</p>
                                                                    <button onClick={(() => { this.chooseRoom(room) })} className="btn btn-outline-warning">Choose that room</button>
                                                                </div>
                                                            )
                                                        })}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <p>{this.state.roomName}</p>
                                <h1 className="text-center">Budget in October 2020</h1>
                                <Cards roomMembers={this.state.roomMembers} roomState={this.state.roomState} />
                            </div>
                        </div>
                    </div>
                    <div>
                        <hr />
                        <div className="row-mainpage">
                            <div className="content-row container">
                                <AddNewExpanseOrDebt value={this.state.selectValue}
                                    onSelectChange={this.onSelectChange}
                                    onMakeExpense={this.onMakeExpense}
                                    onMakeDebt={this.onMakeDebt}
                                    onMakeSettlement={this.onMakeSettlement}
                                    onInputExpanseChange={this.onInputExpanseChange}
                                    onInputDescriptionExpanseChange={this.onInputDescriptionExpanseChange}
                                    onInputDescriptionDebtChange={this.onInputDescriptionDebtChange}
                                    roomMembersWithoutMe={this.state.roomMembersWithoutMe}
                                    actualUserName={this.state.actualUser.name}
                                    onSelectDebtUserChange={this.onSelectDebtUserChange}
                                    onSelectSettlementUserChange={this.onSelectSettlementUserChange} />
                                {this.state.error ?
                                    <Error message={this.state.error} /> : null
                                }
                            </div>
                        </div>
                        <div className="row-mainpage">
                            <div className="content-row container">
                                <h1 className="text-center">Your History Expanses</h1>
                                <History className="text-center" expenseData={this.state.expenseData} getDate={this.getDate} description={this.state.inputDescriptionExpanse} />
                            </div>
                        </div>
                    </div>
                </div >
            </div >

        );
    }
}



export default MainPage;
