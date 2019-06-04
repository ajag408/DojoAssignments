import java.util.ArrayList;
public class Project {
  private String name;
  private String description;
  private double initialCost;

  public Project(){
  }

  public Project(String name){
    this.name = name;
  }

  public Project(String name, String description){
    this.name = name;
    this.description = description;
  }

  //getters

  public String getName(){
    return name;
  }

  public String getDescription(){
    return description;
  }

  public void setName(String name){
    this.name = name;
  }

  public void setDescription(String description){
    this.description = description;
  }

  public double getInitialCost(){
    return initialCost;
  }

  public void setInitialCost(double price){
    initialCost = price;
  }


  public String elevatorPitch(){
    return name + " (" + initialCost + "): " + description;
  }


}

class Portfolio{
  ArrayList<Project> project = new ArrayList<Project>();

  public Portfolio(){
  }

  //setter

  public void addProject(Project projectIn){
    project.add(projectIn);
  }

  public double getPortfolioCost(){
    double total = 0.0;
    double thisCost;
    for(int i = 0; i<project.size(); i++){
      thisCost = project.get(i).getInitialCost();
      total = total + thisCost;
    }
    return total;
  }

  public void showPortfolio(){
    String pitch;
    for(int i = 0; i<project.size(); i++){
      pitch = project.get(i).elevatorPitch();
      System.out.println(pitch);
    }

    double totalCost = this.getPortfolioCost();
    System.out.println(totalCost);
  }
}
