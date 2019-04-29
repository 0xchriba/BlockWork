pragma solidity ^0.4.24;

contract Test1 {



    string Contractor = "";
    string Freelancer = "";
    string Project_Desc = "";
    string Project_Title = "";
    int Project_Amount = -1;
    string Status = "initialized";
    string Project_Code = "";


    event State (
        string Contractor,
        string Freelancer,
        string Project_Desc,
        string Project_Title,
        int Project_Amount,
        string Status,
        string Project_Code
    );

    string Dispute_Method = "";

    constructor() public {
        Contractor = "";
        Freelancer = "";
        Project_Desc = "";
        Project_Title = "";
        Project_Amount = -1;
        Status = "initialized";
        Project_Code = "";
        emit State(Contractor, Freelancer, Project_Desc, Project_Title, Project_Amount, Status, Project_Code);
    }


    function Generate (
        string _c, string _f, string _p_title, string _p_desc, int _p_amt, string _s)
    public {
      Contractor = _c;
      Freelancer = _f;
      Project_Desc = _p_title;
      Project_Title = _p_desc;
      Project_Amount = _p_amt;
      Status = _s;
      emit State(Contractor, Freelancer, Project_Desc, Project_Title, Project_Amount, Status, Project_Code);
    }

    function Project_Status (
    )public view returns (string c, string f, string p_title, string p_desc, string s){
      return (Contractor, Freelancer, Project_Title, Project_Desc, Status);
    }

}
