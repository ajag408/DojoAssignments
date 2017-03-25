//
//  ToDoListViewController.swift
//  toDoList
//
//  Created by Akash Jagannathan on 3/23/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit
import CoreData

class ToDoListViewController: UITableViewController, AddItemViewControllerDelegate{
    
    let managedObjectContext = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
    
    var items = [ToDoListItem]()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        FetchAllItems()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func FetchAllItems(){
        let request = NSFetchRequest<NSFetchRequestResult>(entityName: "ToDoListItem")
        do{
            let results = try managedObjectContext.fetch(request)
            items = results as! [ToDoListItem]
        } catch {
            print(error)
        }
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return items.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ToDoItemCustomCell") as! ToDoItemCustomCell
        
        cell.ItemTitle.text = items[indexPath.row].title

        cell.ItemNotes.text = items[indexPath.row].itemDescription
        
        let mydateFormatter = DateFormatter()
        mydateFormatter.dateFormat = "MM/dd/yyyy"
        mydateFormatter.timeZone = TimeZone.ReferenceType.local
        let dateInString:String = mydateFormatter.string(from: items[indexPath.row].completionDate as! Date)
        
        cell.FinishByDate.text = dateInString
        
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath)
    {
        if tableView.cellForRow(at: indexPath)?.accessoryType == UITableViewCellAccessoryType.checkmark
        {
            tableView.cellForRow(at: indexPath)?.accessoryType = UITableViewCellAccessoryType.none
        }
        else
        {
            tableView.cellForRow(at: indexPath)?.accessoryType = UITableViewCellAccessoryType.checkmark
        }
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let controller = segue.destination as! AddItemViewController
        controller.delegate = self
    }
    
    func addItemViewController(by controller: AddItemViewController, itemTitle: String, itemDescription: String, completionDate: NSDate) {
        let newItem = ToDoListItem(context: managedObjectContext)
        newItem.title = itemTitle
        newItem.itemDescription = itemDescription
        newItem.completionDate = completionDate as NSDate
        do{
            try managedObjectContext.save()
        }catch{
            print(error)
        }
        FetchAllItems()
        tableView.reloadData()
        dismiss(animated: true, completion: nil)
    }
    
}
