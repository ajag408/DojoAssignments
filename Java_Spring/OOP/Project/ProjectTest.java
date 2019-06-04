public class ProjectTest{
    public static void main(String[] args) {
      Project flyEagle = new Project("Air1", "Secret service");
      String squeal = flyEagle.elevatorPitch();
      // System.out.println("Full constructor: " + squeal);
      Project nump = new Project();
      String tight = nump.elevatorPitch();
      // System.out.println("Minimal constructor: " + tight);
      nump.setName("Chump");
      nump.setDescription("To eliminate rascals");
      String tight1 = nump.getName();
      String tight2 = nump.getDescription();
      // System.out.println("getter test 1: " + tight1);
      // System.out.println("getter test 2: " + tight2);
      String tightNew = nump.elevatorPitch();
      // System.out.println("minimal constructor after setters " + tightNew);
      Project flyOne = new Project("RedEagle");
      String redOne = flyOne.elevatorPitch();
      // System.out.println("Middle constructor: " + redOne);
      Portfolio myPortfolio = new Portfolio();
      myPortfolio.addProject(flyEagle);
      myPortfolio.addProject(nump);
      myPortfolio.addProject(flyOne);
      // myPortfolio.showPortfolio();
      flyEagle.setInitialCost(2.3);
      nump.setInitialCost(5.0);
      myPortfolio.showPortfolio();
    }
}
