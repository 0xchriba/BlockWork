pragma solidity ^0.4.24;

contract Test2 {



    string Contractor = "";
    string Freelancer = "";
    string Project_Desc = "";
    string Project_Title = "";
    int Project_Amount = -1;
    string Status = "Initialized";
    string Project_Code = "";
    string Dispute_Method = "";
    bool[] Milestones_Completed;
    bytes32[] Milestone_Descriptions;


    event State (
        string Status,
        string Project_Code,
        bool[] Milestones_Completed,
        bytes32[] Milestone_Descriptions
    );


    // string[] Arbitrators;
    // uint[] Votes;
    // bool[] Voted;


    constructor() public {
        Contractor = "";
        Freelancer = "";
        Project_Desc = "";
        Project_Title = "";
        Project_Amount = -1;
        Status = "Initialized";
        Project_Code = "";
        emit State(Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
    }

    /*Note to get rid of Freelancer */
    function Generate (
        string _c, string _p_title, string _p_desc, int _p_amt, string _s, bool[] _m_comp, bytes32[] _m_desc)
    public {
      Contractor = _c;
      Project_Desc = _p_title;
      Project_Title = _p_desc;
      Project_Amount = _p_amt;
      Status = _s;
      Milestones_Completed = _m_comp;
      Milestone_Descriptions = _m_desc;

      emit State(Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
    }

    function Project_Status (
    )public view returns (string s, string p_code, bool[] m_comp, bytes32[] m_desc){
      return (Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
    }

    function Project_Info (
    )public view returns (string c, string f, string p_title, string p_desc, int p_amt){
      return (Contractor, Freelancer, Project_Title, Project_Desc, Project_Amount);
    }


    function Complete_Milestone (
      int _i, /* index of milestone */ string _p_code, string _s) public {
      Milestones_Completed[uint256(_i)] = true;
      Project_Code = _p_code;
      Status = _s;
      emit State(Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
    }


    function Accept (
        string _f, string _s)   /* optional parameter */
    public {
      Freelancer = _f;
      Status = _s;
      emit State(Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
    }


    function Finish_Project (
        string _s)    /* parameter needed for linking assets and transactions */
    public returns(int p_amt, string p_code){
      Status = _s;
      emit State(Status, Project_Code, Milestones_Completed, Milestone_Descriptions);
      return (Project_Amount, Project_Code);

    }





    // function Raise_Dispute (
    //     bool _isContractor,
    //     string _s,
    //     bytes32[] _arbitrators)   /* have to run conversion */
    // public {
    //   Arbitrators = _arbitrators;
    //   for (uint i = 0; i < proposalNames.length; i++) {
    //     // `Proposal({...})` creates a temporary
    //     // Proposal object and `proposals.push(...)`
    //     // appends it to the end of `proposals`.
    //     proposals.push(Proposal({
    //         name: proposalNames[i],
    //         voteCount: 0
    //     }));
    //   Status = _s;
    // }




    // function Resolve_Dispute (
    //     string assetId, /* parameter needed for linking assets and transactions */
    //     string Outcome)   /* optional parameter */
    // public {}





    // function Negotiate (
    //     string assetId, /* parameter needed for linking assets and transactions */
    //     string _p_desc, /* optional parameter */
    //     int _p_amt, string _s)   /* optional parameter */
    // public {
    //   Project_Desc = _p_desc;
    //   Project_Amount = _p_amt;
    //   Status = _s;

    // }
}
