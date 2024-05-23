using System;

class Fighter {
  public string Name;
  public string FavoriteWeapon;
  public float EXP;
  // EXP is Experience Points
  public int HP;
  public int HPGain;
  public int DefendedAttack;
  public int Defense;
  public int MaxDefense;
  public int Damage;
  Random random = new Random();
  
  public Fighter(string _Name, string _FavoriteWeapon) {
    Name = _Name;
    FavoriteWeapon = _FavoriteWeapon;
    Defense = 0;
    MaxDefense = 10;
    EXP = 0f;
    HP = 100;
  }

  public void attackH() {
    Console.WriteLine(Name + " attacks an enemy using " + FavoriteWeapon + " and deals " + Damage + " Damage");
  }
  public void defendH() {
    if (Defense < MaxDefense)
    {
      Defense += random.Next(1, 3); //so that defense takes a while to build up
      Console.WriteLine("Current defense: " + Defense);
    }
    Console.WriteLine(Name + " is on guard");
  }
  public void healH() {
    HPGain = random.Next(2, 8);
    Console.WriteLine(Name + " heals and regains " + HPGain);
    HP = HP + HPGain;
  }
}

class Boss {
  public string Name;
  public string Weapon;
  public int HPE;
  //the E stands for enemy
  public int HPGainE;
  public int Power;
  public int bossChoice;

  public Boss(string _Name, string _Weapon, int _HPE) {
    Name = _Name;
    Weapon = _Weapon;
    HPE = _HPE;
  }
  
  public void attackE() {
    if (HPE > 0)
    {
    Console.WriteLine(Name + " attacks the hero using " + Weapon + " and deals " + Power + " Damage");
    }
    else {
      Console.Clear();
      Console.WriteLine("Dario: Oh, papa Pedro!");
      System.Threading.Thread.Sleep(1500);
      Console.WriteLine("Dario: It seems like this is the end of the road for me.");
      System.Threading.Thread.Sleep(2000);
    }
}
  
  public void healE() {
    if (HPE > 0)
    {
    Console.WriteLine(Name + " heals and regains " + HPGainE);
    HPE = HPE + HPGainE;
    }
    else {
      Console.Clear();
      Console.WriteLine("Dario: Oh, papa Pedro!");
      System.Threading.Thread.Sleep(1500);
      Console.WriteLine("Dario: It seems like this is the end of the road for me. So long... But a new form of me will come back!");
      System.Threading.Thread.Sleep(2000);
    }
  }

}



class Program {
  public static void Main (string[] args) {
    Console.WriteLine("Loading..");
    System.Threading.Thread.Sleep(10000);
    Console.Clear();
    Random random = new Random();
    bool loop = true;
    string action = "";
    Fighter you = new Fighter("Player", "Rage Scythe");
    you.DefendedAttack = random.Next(1,6); //if we set the variables this early, someone could be able to exploit the rng by reading them and doing the move that yields the best results
    
    Boss dario = new Boss("Dario", "Blaze Slasher", 50);
    //dario.Name = "Dario";
    //dario.Weapon = "Blaze Slasher";
    //dario.HPE = 50;
    dario.HPGainE = random.Next(1,10);
    dario.Power = random.Next(6,13);
    while (loop == true) {
      Console.WriteLine("Boss Battle!!");
      Console.WriteLine("Boss: Dario (Very original name!!)");
      Console.WriteLine("Boss Health: " + dario.HPE);
      Console.WriteLine("Your health: " + you.HP);
      Console.WriteLine("Choose a letter to do an action: \na) Attack! \nb) Defend\nc) Heal ");
      action = Console.ReadLine();
      action = action.ToLower();
      if (action == "a") {
        //Console.Clear();
        you.Damage = random.Next(4,11);
        you.attackH();
        dario.HPE = dario.HPE - you.Damage;
        System.Threading.Thread.Sleep(1500);
        dario.bossChoice = random.Next(1,3);
        System.Threading.Thread.Sleep(1500);
        Console.Clear();
      }
      if (action == "b") {
        //Console.Clear();
        you.defendH();
        System.Threading.Thread.Sleep(1500);
        dario.bossChoice = random.Next(1,3);
        System.Threading.Thread.Sleep(1500);
        Console.Clear();
      }
      if (action == "c") {
        //Console.Clear();
        you.healH();
        System.Threading.Thread.Sleep(1500);
        dario.bossChoice = random.Next(1,3);
        System.Threading.Thread.Sleep(1500);
        Console.Clear();
      }
      
      if (dario.bossChoice == 1) {
        dario.attackE();
        int damageAfterDefense = dario.Power - you.Defense;
        you.HP = you.HP - damageAfterDefense;
        System.Threading.Thread.Sleep(1500);
        Console.Clear();
      }
      if (dario.bossChoice == 2) {
        // dario.HPE;
        dario.healE();
        System.Threading.Thread.Sleep(1500);
        Console.Clear();
      }
      if (dario.HPE <= 0) {
       //just in case enemy hp is a negative number
        loop = false;
      }
      
      
  }
    Console.Clear();
    Console.WriteLine("You beat Dario! New boss coming soon.");
  }
} //Main class bracket
